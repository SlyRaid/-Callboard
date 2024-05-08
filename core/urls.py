from django.urls import path
from core import views


urlpatterns = [
    path('time/', views.current_datetime),
    path('', views.index),
]