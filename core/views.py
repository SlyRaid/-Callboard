from django.shortcuts import render
from django.http import HttpResponse
import datetime

from core import models


def current_datetime(request):
    now = datetime.datetime.today().strftime('%d.%m.%Y %H:%M')
    html = f"Сейчас {now}."
    return HttpResponse(html)

def index(request):
    car_info = models.Car.objects.all()
    student_info = models.Student.objects.all()
    context = {
        'title': 'Списки',
        'cars': 'Список машин',
        'students': 'Список студентов',
        'car_info': car_info,
        'student_info': student_info,
    }
    return render(request, 'core/index.html', context=context)

