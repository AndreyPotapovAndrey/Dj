import pytest
from rest_framework.test import APIClient
from model_bakery import baker
import random

from students.models import Student, Course


@pytest.fixture  # Фикстуры - специальные функции, которые возвращают некоторое значение. И мы их можем использовать в
# качестве аргументов в нашу тестирующую функцию.
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_course(client, course_factory):
    # Arrange - подготовка данных
    course = course_factory(_quantity=1)
    course_id = course[0].id
    # Act - непосредственно тестирование
    response = client.get(f'/api/v1/courses/{course_id}/')
    # Assert - проверка, что действие прошло корректно
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == course_id


# Проверка получения списка курсов:
@pytest.mark.django_db
def test_courses(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get(f'/api/v1/courses/')
    data = response.json()

    assert response.status_code == 200

    for index, course in enumerate(data):
        assert courses[index].id == course['id']


# Проверка фильтрации списка курсов по id:
@pytest.mark.django_db
def test_filter_id(client, course_factory):
    courses = course_factory(_quantity=10)  # В courses у нас 10 экземпляров, которые созданы фабрикой
    indexes = [item.id for item in courses]  # Здесь цикл из 10 id
    index = random.choice(indexes)  # Выбирается один из 10 id случайным образом

    response = client.get(f'/api/v1/courses/?id={index}')  # Здесь мы получаем в переменную response ...?
    data = response.json()

    assert response.status_code == 200
    assert index == data[0]['id']


# Проверка фильтрации списка курсов по name:
@pytest.mark.django_db
def test_filter_name(client, course_factory):
    courses = course_factory(_quantity=10)
    names = [item.name for item in courses]
    name = random.choice(names)

    response = client.get(f'/api/v1/courses/?name={name}')
    data = response.json()
    assert response.status_code == 200
    assert name == data[0]['name']


# Тест успешного создания курса:
@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    data = {
        'name': 'Python-разработчик с нуля'
    }

    response = client.post('/api/v1/courses/', data=data)

    assert response.status_code == 201
    assert Course.objects.count() == count + 1


# Тест успешного обновления курса:
@pytest.mark.django_db
def test_patch_course(client, course_factory):
    course = course_factory(_quantity=1)
    index = course[0].id

    data = {
        'name': 'Python-разработчик с нуля'
    }

    response = client.patch(f'/api/v1/courses/{index}/', data=data)

    assert response.status_code == 200
    assert response.json()['name'] == data['name']


# Тест успешного удаления курса:
@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(_quantity=1)
    index = course[0].id

    response = client.delete(f'/api/v1/courses/{index}/')

    assert response.status_code == 204
