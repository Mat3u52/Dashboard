from django.urls import path
from . import views
from .views import GuidelineViews, GuideCommentView, GuideListView

urlpatterns = [
    # path('', views.guideline_list, name='guideline_list'),
    path('', GuideListView.as_view(), name='guideline_list'),
    path('guideline/<int:pk>', views.guideline_detail, name='guideline_detail'),
    path('guideline/<int:pk>/comment/', GuideCommentView.as_view(), name='guideline_comment'),
    path('guideline/new/', views.guide_new, name='guide_new'),
    path('guideline/<int:pk>/edit/', views.guideline_edit, name='guideline_edit'),
    path('guideline/guideline_search/', views.guideline_search, name='guideline_search'),
    path('guideline/<int:pk>/guideline_share/', views.guideline_share, name='guideline_share'),
    path('cart-items/', GuidelineViews.as_view()),
    path('cart-items/<int:pk>', GuidelineViews.as_view()),
]
