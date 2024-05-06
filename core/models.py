from django.db import models


class Car(models.Model):
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    name = models.CharField('Имя', max_length=255)
    age = models.IntegerField('Возраст')
    grade = models.FloatField('Оценка')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


    def __str__(self) -> str:
        return self.name