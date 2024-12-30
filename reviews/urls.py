from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reviews/', views.review_list, name='review_list'),
]
