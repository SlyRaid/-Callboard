from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePageView.as_view()),
    path('mark/<int:marka_id>', ClassGetMark.as_view()),
    path('car/', CarDetail.as_view(), name='Car'),
    path('form_example/', SimpleForm.as_view(), name='form_example')
]
