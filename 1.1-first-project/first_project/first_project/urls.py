"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from app.views import home_view, time_view, workdir_view, hello, sum, privet, pagi, hello_view, create_car, list_car, \
    create_person, list_person


urlpatterns = [
    path('', home_view, name='home'),
    # Раскомментируйте код, чтобы данные урлы 
    # обрабатывались Django
    path('current_time/', time_view, name='time'),
    path('workdir/', workdir_view, name='workdir'),
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('sum/<int:a>/<int:b>/', sum),# a и b - параметры переданы в функцию sum. int - конвертер. Данный маршрут /
    # сработает, только если в параметрах будут целые числа
    path('privet/', privet),
    path('pagi/', pagi),
    path('hello_view/', hello_view),
    path('new_car/', create_car),
    path('cars/', list_car),
    path('new_person/', create_person),
    path('people/', list_person),
]




