from django_filters import rest_framework as filters
from django.contrib.auth import get_user_model
from advertisements.models import Advertisement
from .fields import CustomDateRangeField

User = get_user_model()


class CustomDateRangeFilter(filters.DateFromToRangeFilter):
    field_class = CustomDateRangeField


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = filters.DateFromToRangeFilter()
    # created_at = CustomDateRangeField
    creator = filters.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']
