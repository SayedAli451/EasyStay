from django.urls import path
from . import views
from .views import room_list
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', room_list, name='room_list'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='hotel/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),

]
