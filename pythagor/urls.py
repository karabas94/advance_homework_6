from django.urls import path

from . import views

app_name = 'pythagor'
urlpatterns = [
    path('', views.index, name='index'),
    path('triangle/', views.triangle, name='triangle'),
    path('hypotenuse/', views.hypotenuse, name='hypotenuse'),
    path('person/result/', views.contact_form_result, name='result'),
    path('person/', views.contact_form, name='user_form'),
    path('person_detail/<int:pk>/', views.contact_form_detail, name='people_detail'),
    path('person/<int:pk>/', views.contact_form_edit, name='people_edit'),
    path('person_delete/<int:pk>/', views.contact_form_delete, name='people_delete'),
]
