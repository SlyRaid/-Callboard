from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime

from core import models


def current_datetime(request):
    now = datetime.datetime.today().strftime('%d.%m.%Y %H:%M')
    html = f"Сейчас {now}."
    return HttpResponse(html)


def index(request):
    car_info = models.Car.objects.all()
    mark_info = models.Marka_car.objects.all()
    context = {
        'title': 'Марки',
        'cars': 'Список машин',
        'car_info': car_info,
        'mark_info': mark_info,
    }
    return render(request, 'core/index.html', context=context)


def get_mark(request, marka_id):
    car_info = models.Car.objects.filter(marka=marka_id)
    mark_info = models.Marka_car.objects.all()
    marka = models.Marka_car.objects.get(pk=marka_id)
    context = {
        'marka': marka,
        'car_info': car_info,
        'mark_info': mark_info,
    }
    return render(request, 'core/marka.html', context=context)


# def show_mark(request, marka_id):
#     mark = get_object_or_404(models.Marka_car, pk=marka_id)
#     context = {
#         'marka': mark.title,
#     }
#     return render(request, )