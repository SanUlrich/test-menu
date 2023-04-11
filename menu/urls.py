from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<str:slug>/', views.activate_menu, name='activate_menu'),
]
