from django.urls import path

from . import views

app_name = 'eradicate'
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
]