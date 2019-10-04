from django.shortcuts import render, get_object_or_404, redirect
from hashlib import md5
import logging
# hashlib.md5(b"password")
from django.utils import timezone
from django.shortcuts import HttpResponse
from django.db import Error
from django.http import Http404
from django.utils.decorators import method_decorator
from django.utils.http import urlencode
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.views import APIView

from backend.courses.models import Course

from .models import Pay
from django.views import View

logging.basicConfig(
    filename='log/pay.log',
    format="%(levelname)-10s %(lineno)d %(asctime)s %(message)s",
    level=logging.INFO
)

log = logging.getLogger('pay')

allow_ips = [
    '136.243.38.147',
    '136.243.38.149',
]

PAYMENT = {
    'aggregator': 'free-kassa',
    'merchant_id': '23451',
    'secret_key': '1ndfshnr',
    'secret_key2': 'mrwtbgveeg',
    'currency': 'RUB'
}


BUBBLE = {
    'site_title': 'Django Channel',
    'project_name': 'Django Channel',
    'server_ip': 'djangochannel.com',
    'keywords': 'Django',
    'description': 'Donation system written with Django',
    'description_of_project': 'Donation system written with Django',
    'description_of_purchase': 'Покупка {item} для {account} на {project_name}',
    'message_of_pending': 'Ожидается выполнение платежа!',
    'message_of_success': 'Поздравляем с покупкой!',
    'message_of_fail': 'Что-то пошло не так. Попробуйте ещё раз!'
}

args = BUBBLE
args.update({
    'items': Course.objects.all()
})


required_params = [
    'MERCHANT_ID',
    'AMOUNT',
    'intid',
    'MERCHANT_ORDER_ID',
    'CUR_ID',
    'SIGN',
    'us_item'
]


class Payment(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        log.info('запущен')
        ip = request.META.get('HTTP_CF_CONNECTING_IP')
        if ip is None:
            ip = request.META.get('REMOTE_ADDR')
        log.info("ip - {}".format(ip))
        # if ip not in allow_ips:
        #     raise Http404()

        # if any(required_param not in request.GET for required_param in required_params):
        #     return HttpResponse('Invalid request')

        data = request.POST.copy()
        log.info("data - {}".format(data))
        key = PAYMENT['secret_key2']
        account = data.get('MERCHANT_ORDER_ID')

        if data.get('us_item'):
            item_id = int(data.get('us_item'))
        else:
            item_id = 1

        if data.get('intid') == 'TEST_ORDER':
            payment_id = data.get('intid')
        else:
            payment_id = int(data.get('intid'))

        order_sum = int(data.get('AMOUNT'))

        # except ValueError:
        #     return HttpResponse('Invalid parameters')

        sign_string = ':'.join((data.get('MERCHANT_ID'), data.get('AMOUNT'), key, account))
        sign = md5(sign_string.encode('utf-8')).hexdigest()

        if data.get('SIGN') != sign:
            return HttpResponse('Incorrect digital signature')

        if data.get('MERCHANT_ID') != PAYMENT['merchant_id']:
            return HttpResponse('Invalid checkout id')

        try:
            course = Course.objects.get(id=item_id)
        except Course.DoesNotExist:
            return HttpResponse('Not course')

        if order_sum != course.price:
            return HttpResponse('Invalid payment amount')

        try:
            payment = Pay.objects.get(id=data.get('us_pay'))
            payment.status = 1
            payment.date_complete = timezone.now()
            payment.save()

            course.students.add(payment.account)
            course.save()

            return HttpResponse('YES')
        except Pay.DoesNotExist:
            return HttpResponse('Unable to create payment database')

        # else:
        #     return HttpResponse('Payment has already been paid')


class Initialization(View):
    def post(self, request):
        form = request.POST

        item = get_object_or_404(Course, id=form.get('item'))

        merchant_id = PAYMENT['merchant_id']
        secret_key = PAYMENT['secret_key']
        currency = PAYMENT['currency']
        item_id = form.get('item')
        account = str(request.user) # form.get('account')
        price = str(item.price)
        desc = args['description_of_purchase'].format(
            item=item.title,
            account=account,
            project_name=args['project_name']
        )

        paym = Pay()
        paym.account = request.user
        paym.item = item
        paym.status = 0
        paym.save()

        separator = ':'
        params = {
            'm': merchant_id,
            'oa': price,
            'o': account,
            'i': currency,
            'us_item': item_id,
            'us_pay': paym.id
        }

        sign_string = separator.join((merchant_id, price, secret_key, account))

        sign = md5(sign_string.encode('utf-8')).hexdigest()
        params.update({'s': sign})

        params_string = urlencode(params)

        url = 'https://www.free-kassa.ru/merchant/cash.php?{}'
        return redirect(url.format(params_string))


def index(request):
    return render(request, 'pay/form.html', args)


def pending(request):
    return render(request, 'pay/pending.html', args)


def success(request):
    return render(request, 'pay/success.html', args)


def fail(request):
    return render(request, 'pay/fail.html', args)


class DonateView(View):
    """Донат на сайте"""
    def get(self, request):
        return render(request, 'pay/donate.html')
