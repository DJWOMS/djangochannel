from django.core.management.base import BaseCommand

from moderation.models import SimpleRight


class Command(BaseCommand):
    """Создание в базе возможных прав для модераторов"""
    help = 'Creating simple rights for moderators'

    def create_simple_rights(self):
        rights = {
            0: 'Полные права',
            1: 'Возможность запретить комментирование',
            2: 'Возможность запретить создание топиков',
            3: 'Возможность запретить доступ к форуму',
            4: 'Возможность редактирования топиков',
            5: 'Возможность удаления топиков',
            6: 'Возможность удаления комментариев',
        }

        for k, v in rights.items():
            if not SimpleRight.objects.filter(key=k).exists():
                SimpleRight.objects.create(key=k, description=v)
                self.stdout.write('"{}" добавлено'.format(v))
            else:
                self.stdout.write('Запись с ключом {} уже существует'.format(k))

    def handle(self, *args, **options):
        self.create_simple_rights()
        self.stdout.write('Завершено')
