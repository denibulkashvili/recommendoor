from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('review/<int:pk>/', views.review_detail, name='review_detail'),
    path('company/', views.company_list, name='company_list'),
    path('company/<int:pk>/', views.company_detail, name='company_detail'), 
]