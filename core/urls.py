from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import *

app_name = 'core'

router = DefaultRouter()
router.register(r'carlist', CarView)

urlpatterns = [
    # path('', HomePageView.as_view()),
    # path('mark/<int:marka_id>', ClassGetMark.as_view()),
    # path('car/', CarDetail.as_view(), name='Car'),
    # path('form_example/', SimpleForm.as_view(), name='form_example'),
    # path('api/carlist/', CarView.as_view()),
    # path('api/carlist/<int:pk>/', CarView.as_view()),
]

urlpatterns += router.urls
