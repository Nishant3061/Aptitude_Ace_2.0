from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('check_answer/', views.check_answer, name='check_answer'),
]
