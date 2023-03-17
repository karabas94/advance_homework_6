from django.urls import path

from . import views

app_name = 'pythagor'
urlpatterns = [
    path('', views.index, name='index'),
]