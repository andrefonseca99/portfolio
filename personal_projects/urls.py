from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about-me/', views.about, name="about"),
    path('my-work/', views.work, name="work"),
    path('contact/', views.contact, name="contact"),
]
