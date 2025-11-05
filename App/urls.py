from django.urls import path
from .views import *

urlpatterns = [
    path("", test, name="index"),
    path('success',success,name='success')
]