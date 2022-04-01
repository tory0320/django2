from django.urls import path
from . import views

urlpatherns = [
    path('about_me/', views.about_me),
    path('', views.landing),
]