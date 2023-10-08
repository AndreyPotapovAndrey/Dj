from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    """ Общий каталог с возможностью сортировки. """
    template = 'catalog.html'
    sort_param = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }[request.GET.get('sort', 'name')]

    phones = Phone.objects.all().order_by(sort_param)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    """ Описание конкретного товара. """
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)[0]
    context = {'phone': phone}
    return render(request, template, context)
