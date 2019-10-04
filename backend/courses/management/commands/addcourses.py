from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import User

from backend.courses.models import Category, Course


# User = settings.AUTH_USER_MODEL


class Command(BaseCommand):
    """Добавление категорий и курсов"""
    help = 'Add superuser'

    def handle(self, *args, **options):
        user = User.objects.get(id=1)

        cat = Category.objects.create(title="Python 3")
        Category.objects.create(title="Django 2")
        Category.objects.create(title="JavaScript")
        Category.objects.create(title="Vue 2")
        Category.objects.create(title="HTML 5")
        Category.objects.create(title="CSS 3")

        Course.objects.create(
            title="Python 3 for beginners",
            category=cat,
            description="""Python – простой, гибкий и невероятно популярный язык, который используется практически
             во всех областях современной разработки. С его помощью можно создавать веб-приложения, писать игры, 
             заниматься анализом данных, автоматизировать задачи системного администрирования и многое другое. 
             'Погружение в Python' читают разработчики, применяющие Python в проектах, которыми ежедневно пользуются\
             миллионы людей. Курс покрывает все необходимые для ежедневной работы программиста темы, 
             а также рассказывает про многие особенности языка, которые часто опускают при его изучении.
             В ходе курса вы изучите конструкции языка, типы и структуры данных, функции, 
             научитесь применять объектно-ориентированное и функциональное программирование, 
             узнаете про особенности реализации Python, научитесь писать асинхронный и многопоточный код. 
             Помимо теории вас ждут практические задания, которые помогут проверить полученные знания и отточить навыки 
             программирования на Python. После успешного окончания курса вы сможете использовать полученный опыт для 
             разработки проектов различной сложности.""",
            price=15000,
            date_start="2019-06-01",
            instructor=user)

        self.stdout.write('Success')
