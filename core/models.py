from django.db import models
from django.urls import reverse


class Car(models.Model):
    TYPE_CHOICE = (
        ('hatchback', 'хэтчбек'),
        ('saloon', 'седан'),
        ('estate', 'универсал'),
        ('convertible', 'кабриолет')
    )

    car_name = models.CharField('Название', max_length=100)
    car_body = models.CharField('Кузов', max_length=100, choices=TYPE_CHOICE, null=True)
    information = models.TextField('Информация', null=True, blank=True)
    car_img = models.ImageField('Фото', upload_to='media', null=True, blank=True)

    marka = models.ForeignKey('Marka_car', on_delete=models.CASCADE, verbose_name='Марка', null=True)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self) -> str:
        return self.car_name

    def get_full_name(self):
        name = f'{self.marka} {self.car_name}'
        return name

class Marka_car(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Марка машины')

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'
        ordering = ['title']

    def __str__(self) -> str:
        return self.title
