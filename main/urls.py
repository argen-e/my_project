from django.contrib import admin
from django.urls import path, include
from .views import (
    home,
    read_data,
    update_data,
    delete_data,
)

app_name = 'main'

urlpatterns = [
    path('create/', home, name='home'),
    path('read/', read_data, name='read'),
    path('update/<str:pk>', update_data, name='update'),
    path('delete/', delete_data)
]
