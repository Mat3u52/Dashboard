from django.urls import path
from . import views
from .views import GuidelineViews

urlpatterns = [
    # path('', views.guideline_list, name='guideline_list'),
    path('', views.GuideListView.as_view(), name='guideline_list'),
    path('guideline/<int:pk>', views.guideline_detail, name='guideline_detail'),
    path('guideline/new/', views.guide_new, name='guide_new'),
    path('guideline/<int:pk>/edit/', views.guideline_edit, name='guideline_edit'),
    path('cart-items/', GuidelineViews.as_view()),
    path('cart-items/<int:pk>', GuidelineViews.as_view()),
]
