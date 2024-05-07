from django.db import models


class Car(models.Model):

    TYPE_CHOICE = (
        ('hatchback', 'хэтчбек'),
        ('saloon', 'седан'),
        ('estate', 'универсал'),
        ('convertible', 'кабриолет')
    )

    car_name = models.CharField('Название', max_length=100)
    car_body = models.CharField('Кузов', max_length=100, choices=TYPE_CHOICE, default='saloon')
    information = models.TextField('Информация', null=True, blank=True)


    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


    def __str__(self) -> str:
        return self.car_name


class Student(models.Model):
    first_name = models.CharField('Фамилия', max_length=20, default='')
    last_name = models.CharField('Имя', max_length=10, default='')
    age = models.PositiveIntegerField('Возраст')

    grade = models.FloatField('Оценка')
    expelled = models.BooleanField('Исключен', default=False)


    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
