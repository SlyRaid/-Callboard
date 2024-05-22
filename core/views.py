from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime

from django.views.generic import TemplateView, ListView, DetailView, RedirectView, FormView

from core import models, forms

from django.urls import reverse


class HomePageView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["car_info"] = models.Car.objects.all()
        context["mark_info"] = models.Marka_car.objects.all()
        return context


class ClassGetMark(TemplateView):
    template_name = 'core/marka.html'

    def get_context_data(self, marka_id, **kwargs):
        context = super().get_context_data(**kwargs)

        context["car_info"] = models.Car.objects.filter(marka=marka_id)
        context["mark_info"] = models.Marka_car.objects.all()
        context["marka"] = models.Marka_car.objects.get(pk=marka_id)
        return context


class CarDetail(ListView):
    model = models.Car
    context_object_name = 'Car'
    template_name = 'core/car_detail.html'

class SimpleForm(FormView):
    template_name = 'core/form.html'
    form_class = forms.SimpleForm
    success_url = "/car/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

# class ClassShowPost():
# def show_mark(request, marka_id):
#     mark = get_object_or_404(models.Marka_car, pk=marka_id)
#     context = {
#         'marka': mark.title,
#     }
#     return render(request, 'core/showpost.html', context)

# def get_mark(request, marka_id):
#     car_info = models.Car.objects.filter(marka=marka_id)
#     mark_info = models.Marka_car.objects.all()
#     marka = models.Marka_car.objects.get(pk=marka_id)
#     context = {
#         'marka': marka,
#         'car_info': car_info,
#         'mark_info': mark_info,
#     }
#     return render(request, 'core/marka.html', context=context)


# def index(request):
#     car_info = models.Car.objects.all()
#     mark_info = models.Marka_car.objects.all()
#     context = {
#         'title': 'Марки',
#         'cars': 'Список машин',
#         'car_info': car_info,
#         'mark_info': mark_info,
#     }
#     return render(request, 'core/index.html', context=context)
