from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
import datetime

from django.views.generic import TemplateView, ListView, DetailView, RedirectView, FormView
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core import models, forms, filters, serializers
from django_filters.rest_framework import DjangoFilterBackend

from django.urls import reverse


# class HomePageView(TemplateView):
#     template_name = 'core/index.html'
#
#     def get_filters(self):
#         return filters.FilterCar(self.request.GET)
#
#     def get_queryset(self):
#         return self.get_filters().qs
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context["car_info"] = models.Car.objects.all()
#         context["mark_info"] = models.Marka_car.objects.all()
#         context["filters"] = self.get_filters()
#         return context
#
#
# class ClassGetMark(TemplateView):
#     template_name = 'core/marka.html'
#
#     def get_context_data(self, marka_id, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context["car_info"] = models.Car.objects.filter(marka=marka_id)
#         context["mark_info"] = models.Marka_car.objects.all()
#         context["marka"] = models.Marka_car.objects.get(pk=marka_id)
#         return context

#
# class CarDetail(ListView):
#     model = models.Car
#     context_object_name = 'Car'
#     template_name = 'core/car_detail.html'
#
#
# class SimpleForm(FormView):
#     template_name = 'core/car_detail.html'
#     form_class = forms.SimpleForm
#     success_url = "/car/"
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)

class CarView(ModelViewSet):
    queryset = models.Car.objects.all()
    filterset_class = filters.FilterCar
    serializer_class = serializers.CarS



# class CarView(generics.ListAPIView):
#     queryset = models.Car.objects.all()
#     serializer_class = serializers.CarS


# class CarView(APIView):
#
#
#     def get(self, request, format=None):
#         snippets = models.Car.objects.all()
#         serializer = serializers.CarS(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = serializers.CarS(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'message': 'OK'})
