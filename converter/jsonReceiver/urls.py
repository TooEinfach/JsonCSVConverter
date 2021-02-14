from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('app_save/', views.app_save, name='app_save'),
]