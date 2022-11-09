from django.urls import path
from . import views

urlpatterns = [
    path('foods/', views.get_foods),
]