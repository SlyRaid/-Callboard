from django.shortcuts import render
from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.today().strftime('%d.%m.%Y %H:%M')
    html = f"Сейчас {now}."
    return HttpResponse(html)

