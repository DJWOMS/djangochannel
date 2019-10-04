from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse


class Pages(models.Model):
    """Страницы"""
    title = models.CharField("Заголовок", max_length=500)
    text = RichTextUploadingField("Текст", blank=True)
    published = models.BooleanField("Опубликовать?", default=True)
    template = models.CharField("Шаблон", max_length=500, default="pages/home.html")
    slug = models.SlugField(
        "URL",
        max_length=500,
        default="",
        help_text="Укажите url",
        unique=True,
        blank=True,
        null=True
    )
    description = models.TextField("Description", max_length=300, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.slug:
            return reverse('page', kwargs={'slug': self.slug})
        else:
            return reverse('page')

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
