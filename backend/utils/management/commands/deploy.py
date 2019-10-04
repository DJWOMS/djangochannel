from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """Выполнение устанвки проекта"""
    help = 'Deploy'

    def handle(self, *args, **options):
        call_command('makemigrations', verbosity=3)
        call_command('migrate', verbosity=3)
        call_command('addposts', verbosity=3)
        self.stdout.write('Success deploy')
