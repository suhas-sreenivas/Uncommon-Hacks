from django.urls import path
from restapi import views

urlpatterns = [
    path('comics/', views.comics_list)
]