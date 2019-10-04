def all_fields(cls, *exclude_fields):
    """
    Для админки Django, дабы избежать муторного перечисления
    всех полей, которые мы хотим вывести:
    list_display = ('any_field', 'any_field2',
        'any_field2', 'any_field3', 'any_field4', any_field5')


    Первый пример использования
    (этот пример выведет все поля модели MyModel):

    from django.contrib import admin
    from .models import MyModel
    from utils.admin import all_fields

    class MyModelAdmin(admin.ModelAdmin):
        list_display = all_fields(MyModel)


    Второй пример использования
    (этот пример выведет все поля модели MyModel,
    кроме 'id' и 'date'):

    from django.contrib import admin
    from .models import MyModel
    from utils.admin import all_fields

    class MyModelAdmin(admin.ModelAdmin):
        list_display = all_fields(MyModel, 'id', 'date')

    """
    return [field.name for field in cls._meta.fields if field.name not in exclude_fields]
