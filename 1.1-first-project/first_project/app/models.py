from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    #owners = ...

    def __str__(self):
        return f'{self.brand}, {self.model}: {self.color}'


class Person(models.Model):
    name = models.CharField(max_length=50)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='owners')  # 1. Связь с таблицей (классом Car)
    # models.ForeignKey является связью один ко многим. У одной машины может быть несколько владельцев. У одного
    # владельца - одна машина.
    # 2. Если вдруг будет удалена запись Car, то будет удалена и таблица (класс) Car.
    # 3. "related_name" - см. 8-ю строку. Нужен чтобы не дублировать в 2-х местах кода.

# Модели и БД не появляются автоматически. Для этого нужно:

# 1. Зарегистрировать приложение, в котором описаны модели (в settings.py)
# 2. Создать файл миграций. Файл миграций описывает, что за изменения должны произойти с БД, чтобы она могла
# соответствовать текущей структуре. python manage.py makemigrations
# 3. Применить миграцию. python manage.py migrate
# 4. После смены базы данных необходимо опять применить миграцию. python manage.py migrate
