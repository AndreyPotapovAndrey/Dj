from django.contrib import admin
from .models import Person, \
    Car  # Для создания административной панели сначала необходимо импортировать таблицы (модели)


@admin.register(
    Car)  # Регистрируем при помощи декоратора класс CarAdmin как административный класс для модели Car при помощи декоратора @admin
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model', 'color', ]  # Какие столбики (поля) будет видно в административной панели (свойство list_display)
    list_filter = ['brand', 'model', ]  # Список свойств, по которым будем фильтровать.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'car', ]
