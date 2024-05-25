import django_filters
from django.db.models import Q

from core import models


class FilterCar(django_filters.FilterSet):
    car_name = django_filters.CharFilter(label='Модель', lookup_expr='icontains')

    class Meta:
        model = models.Car
        fields = ('car_name',
                  'car_body',
                  'marka',
                  )
