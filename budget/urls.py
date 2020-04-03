from django.urls import path
from . import views  # . is current directory

urlpatterns = [
    path('', views.home, name='Budget-home'),
    path('about/', views.about, name='Budge-Manager-About'),
]
