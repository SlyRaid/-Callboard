from django.urls import path

from .views import *


urlpatterns = [
    path('time/', current_datetime),
    path('', index),
    path('mark/<int:marka_id>', get_mark),
]