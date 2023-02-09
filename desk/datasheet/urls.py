from django.urls import path
from . import views

urlpatterns = [
    path('', views.guideline_list, name='guideline_list'),
    path('guideline/<int:pk>', views.guideline_detail, name='guideline_detail'),
]
