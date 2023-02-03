from django.urls import path
from . import views

urlpatterns = [
    path('', views.guideline_list, name='guideline_list'),
]
