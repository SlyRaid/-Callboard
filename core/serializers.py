from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core import models

class CarS(serializers.ModelSerializer):

    # name = serializers.SerializerMethodField()

    class Meta:
        model = models.Car
        fields = '__all__'

    # def get_name(self, obj: models.Car):
    #     return obj.get_full_name()

    # def validate(self, attrs: dict):
    #     if attrs['car_name'] == 'Granta':
    #         raise ValidationError('Страшно, очень страшно, '
    #                               'мы не знаем что это такое, '
    #                               'если бы мы знали, что это такое, '
    #                               'но мы не знаем, что это такое')