import random

from django.core.mail import send_mail, BadHeaderError


def generate(key=None, length=None):
    """Генерация кода"""
    if key is None:
        key = ''
    if length is None:
        length = 32
    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    uletters = letters.upper()
    blank = digits + letters + uletters + key
    lst = list(blank)
    random.shuffle(lst)
    code = ''.join([random.choice(lst) for x in range(length)])
    return code


def send_email(email, code):
    """Отправка кода на email"""
    subject = 'Код подтверждения'
    message = 'Введите этот код для подтверждения смены email: {}'.format(code)
    try:
        send_mail(subject, message, 'robot@djangochannel.com', [email])
        return True
    except BadHeaderError:
        return False


def send_mail_forum(instance):
    """Отправка email о новых темах"""
    subject = 'Новая темя на форуме'
    message = 'Пользователем {}, была создана новая тема "{}" в разделе "{}"'.format(
        instance.user,
        instance.title,
        instance.section)
    try:
        send_mail(subject, message, 'robot@djangochannel.com', ["socanime@gmail.com"])
        return True
    except BadHeaderError:
        return False


def send_mail_contact(instance):
    """Отправка email контакной формы"""
    subject = 'Новое сообщение обратной связи'
    message = 'Пользователем {}, была создана новая тема "{}"'.format(
        instance.email,
        instance.title)
    try:
        send_mail(subject, message, 'robot@djangochannel.com', ["socanime@gmail.com"])
        return True
    except BadHeaderError:
        return False


def send_mail_new_mess(user, email):
    """Отправка email о новом личном сообщении"""
    subject = 'Новое личное сообщение'
    message = 'Здравствуйте, пользователь {}, отправил Вам личное сообщение на сайте djangochannel.com\n ' \
              'Посмотреть его Вы можете у себя в личном кабинете.'.format(user)
    try:
        send_mail(subject, message, 'robot@djangochannel.com', [email])
        return True
    except BadHeaderError:
        return False


def send_mail_mess_student(emails, subj, mess):
    """Отправка email всем участникам курса"""
    subject = subj
    message = mess
    try:
        send_mail(subject, message, 'robot@djangochannel.com', emails, html_message=mess)
        return True
    except BadHeaderError:
        return False


def send_mail_user_post(instance):
    """Отправка email о предложенной статье"""
    subject = 'Предложена новая статья'
    message = 'Пользователем {}, была предложена новая статья "{}" с категорией "{}"'.format(
        instance.author,
        instance.title,
        instance.category
        )
    try:
        send_mail(subject, message, 'robot@djangochannel.com', ["socanime@gmail.com"])
        return True
    except BadHeaderError:
        return False


# def send_mail_edit_password(instance):
#     """Отправка email о смене пароля пользователя"""
#     subject = 'Смена пароля'
#     message = 'Ваш пароль учетной записи "{}" на сайте djangochannel.com, был успешно изменен'.format(instance.user)
#     try:
#         send_mail(subject, message, 'robot@djangochannel.com', ["socanime@gmail.com", 'hamell1987@gmail.com'])
#         return True
#     except BadHeaderError:
#         return False
