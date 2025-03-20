from django.urls import path
from . import views
from .views import room_list

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', room_list, name='room_list'),
]
