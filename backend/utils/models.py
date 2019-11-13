from django.db import models
from django.core.exceptions import ValidationError as DjangoValidationError

from backend.utils.transliteration import transliteration_rus_eng_image as translite


def create_path(instance, filename):
    """Определение пути сохранения изображения"""
    return '{}/{}/{}'.format(instance.__class__.__name__.lower(), translite(instance), filename)


class AbstractImageModel(models.Model):
    """Абстрактная модель изображений"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.min_height = kwargs.get('min_height', 150)
        self.min_width = kwargs.get('min_width', 150)

    height = models.IntegerField(editable=False, null=True)
    width = models.IntegerField(editable=False, null=True)
    image = models.ImageField(
        'Изображение',
        upload_to=create_path,
        height_field='height',
        width_field='width',
        blank=True,
        null=True
    )

    class Meta:
        abstract = True

    def check_size(self):
        """Проверка размера изображения"""
        return False if self.image and (
                self.height < self.min_height or self.width < self.min_width
        ) else True

    def full_clean(self, *args, **kwargs):
        """
        Добавлена логика проверки размеров
        изображения при добавлении через админку
        """
        super().full_clean(*args, **kwargs)

        if not self.check_size():
            raise DjangoValidationError(
                'Размер изображения должен быть не менее {}x{} пикселей'.format(self.min_height, self.min_width)
            )

    # def save(self, *args, **kwargs):
    #     """
    #     Добавлена логика проверки размеров
    #     изображения при добавлении через API
    #     """
    #     if not self.check_size():
    #         raise ValidationError(
    #             detail='Размер изображения должен быть не менее {}x{} пикселей'.format(
    #                 self.min_height, self.min_width),
    #             code=400
    #         )
    #
    #     super().save(*args, **kwargs)
