# from __future__ import absolute_import, unicode_literals
import logging
import os
import sys
import time

import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname("../" + __file__))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'DS.settings'

import django
django.setup()

from django.contrib.auth.models import User

from backend.courses.models import CheckPAyUser, Course

from DS.celery import app


logging.basicConfig(
    filename='log/debug_new.log',
    format="%(levelname)-10s %(lineno)d %(asctime)s %(message)s",
    level=logging.INFO
)

log = logging.getLogger('pay')


# class CheckPay:
@app.task()
def check_api(id, user):
    """Проверка оплаты за курс"""
    t = 60 * 60 * 6
    while t > 0:
        try:
            check = CheckPAyUser.objects.get(status=False, user_id=id)
        except CheckPAyUser.DoesNotExist:
            check = False

        if check:
            key = "G5Aexu9HvlJiuHsZrLSSdNXrlvddhA51EiFIwZOxpXpqELCcEUeVwqk0bdwe"
            payload = {
                "access_token": key,
                "limit": "",
                "before": "",
                "after": "",
                "skip": "",
                "order": "",
                "type": "donation",
                "status": "success",
            }
            url = "https://donatepay.ru/api/v1/transactions"
            r = requests.get(url,  params=payload)
            item = r.json()

            for k in item:
                if k == "data":
                    for data in item[k]:
                        if data.get("what") == user and int(float(data.get("sum"))) == check.summ:
                            check.status = True
                            check.save()
                            course = Course.objects.get(id=check.course_id)
                            course.students.add(User.objects.get(id=id))
                            course.save()
                            log.info("Есть запись - {}".format(user))
                            break
                            # return "{}: {}".format(data.get("what"), data.get("sum"))
        else:
            log.info("Нет записи - {}".format(user))
            time.sleep(20 * 60)
            t -= 20 * 60
            continue

            # return "Нет записи"

# CheckPay().check_api("Дмитрий")