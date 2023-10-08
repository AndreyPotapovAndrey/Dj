from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, reverse
# from datetime import datetime 2-й способ трансляции текущего времени
import datetime
import os
import random

from app.models import Car, Person


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        # 'Показать текущее время': reverse('time_view'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    #     current_time = datetime.now().strftime('%H-%M-%S')
    #     time = f'Текущее время: {current_time}'
    #     return HttpResponse(time)
    current_time = datetime.datetime.now().time()
    return HttpResponse(f'Time = {current_time}')


def workdir_view(request):
    """ Возвращает содержимое рабочей директории (first_project/app/). """
    list_dir = '<br>'.join(os.listdir('first_project/'))
    return HttpResponse(list_dir)


def hello(request):
    name = request.GET.get("name")  # GET - словарь. get - безопасный метод, который позволяет нам достать значение
    # Если значения нет, то вернёт None

    age = int(request.GET.get("age", 33))  # Все параметры являются строковыми. 33 - дефолтное значение. Если не будет
    # найдено значение 35, то вернётся 33.
    print(age)
    return HttpResponse(f'Hello, {name}')


def sum(request, a, b):  # a и b - параметры переданные через URL являются строками
    result = a + b  # int здесь не нужен. Конвертор сам приводит параметры к нужному типу
    return HttpResponse(f'Sum = {result}')


def privet(request):
    context = {
        'test': 5,
        'data': [1, 5, 8],
        'val': 'hello',
    }
    return render(request, 'demo.html', context)


CONTENT = [str(i) for i in range(10000)]  # Список строк из чисел


def pagi(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)  # Класс Paginator. На вход принимает контент (список), 10 элементов на странице
    page = paginator.get_page(page_number)  # Можно получить конкретную страницу
    context = {  # Передадим страницу в контекст, чтобы в шаблоне она была доступна
        'page': page
    }
    return render(request, 'pagi.html', context)


def hello_view(request):
    msg = f'Свяжитесь с админом {settings.CONTACT_EMAIL}'
    return HttpResponse('Всем привет! Я Django! ' + msg)


def create_car(request):
    car = Car(
        brand=random.choice(['B1', 'B2', 'B3']),
        model=random.choice(['M1', 'M2', 'M3']),
        color=random.choice(['C1', 'C2', 'C3']),
    )
    car.save()
    return HttpResponse(f'Все получилось! Новая машина: {car.brand}, {car.model}')


def list_car(request):
    car_objects = Car.objects.all()
    # car_objects = Car.objects.filter(brand__contains='2')  # Если в названии бренда есть 2-ка
    # car_objects = Car.objects.filter(brand__startswith='2')  # Если бренд начинается на 2-ку
    cars = [f'{c.id}: {c.brand}, {c.model}: {c.color} | {c.owners.count()}' for c in car_objects]  # Сколько владельцев
    # у данного авто.
    return HttpResponse('<br>'.join(cars))


def create_person(request):
    cars = Car.objects.all()
    for car in cars:
        # Person.objects.create(name='P', car=car)  # Создать для каждого авто человека. Сначала создаётся объект Person
        # в памяти. Затем сохраняется в базе данных.
        Person.objects.create(name='P', car=car)  # Второй способ создания. Запись в базе данных создаётся сразу же.
    return HttpResponse('Все получилось!')


def list_person(request):
    person_objects = Person.objects.all()
    people = [f'{p.name}: {p.car}' for p in person_objects]
    return HttpResponse('<br>'.join(people))



