from django.urls import path
from . import views

urlpatterns = [
    path('generate-scale/', views.generate_scale, name='generate_scale'),
]