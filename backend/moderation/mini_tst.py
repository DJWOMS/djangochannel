import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname("../" + __file__))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'DS.settings'

import django
django.setup()


from profile.models import UserProfile
from moderation.models import SimpleRight
from moderation.permissions import consts as list_perms

# list_perms = [MINIMAL_BAN, MAXIMAL_BAN, CAN_DELETE]


def foo():
    for profile in UserProfile.objects.all():
        if not profile.is_forum_moderator:
            print('Не модератор', profile.username)
        else:
            print('Модератор', profile.username)
            for perm in list_perms:
                instance = SimpleRight.objects.filter(key__in=perm)
                print(instance.description, ':', instance in profile.user.moderator_rights.rights.all())


if __name__ == '__main__':
    foo().execute()

# foo().execute()
