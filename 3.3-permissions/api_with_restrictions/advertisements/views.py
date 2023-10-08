from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Advertisement
from .permissions import IsOwnerOrReadOnly
from .serializers import AdvertisementSerializer

from django_filters import rest_framework as filters
from .filters import AdvertisementFilter

"""ViewSet для объявлений."""


# TODO: настройте ViewSet, укажите атрибуты для кверисета,
#   сериализаторов и фильтров

class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]  # Список разрешений для манипуляций (разделение прав:
    # кто из пользователей что может делать). Permission-класс IsAuthenticated требует, чтобы пользователь был
    # аутентифицирован. То есть представил свой токен. Класс IsOwnerOrReadOnly проверяет имеет ли право на то или иное
    # действие тот или иной пользователь.


