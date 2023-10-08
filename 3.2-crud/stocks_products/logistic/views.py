from rest_framework.viewsets import ModelViewSet
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(ModelViewSet):
    '''Класс для работы с продуктами'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]  # SearchFilter позволяет искать по тексту
    search_fields = ['title', 'description']  # Поиск продукта в названии и описании


class StockViewSet(ModelViewSet):
    '''Класс для работы со складами'''
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['products']
    search_fields = ['products__title', 'products__description']  # Поиск склада по (идентификатору) названию продукта
    # или по словам в описании