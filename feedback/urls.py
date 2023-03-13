from django.urls import path, include
from .views import *

urlpatterns = [
    path('name/', get_name, name='get_name')
]