from django.urls import path
from . import views

urlpatterns = [
    path('', views.smart_analysis, name='smart_analysis'),
]
