from django.urls import path
import views

urlspatterns = [
    path('', views.landing, name='landing')
]