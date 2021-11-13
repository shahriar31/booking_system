from django.urls import path
from .views import *

urlpatterns = [
    path('create', BookingCreateAPIView.as_view()),
]