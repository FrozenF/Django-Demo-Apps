# portfolio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.portofolio, name='portofolio'),
    path('create', views.create_portofolio_item, name='create_portofolio'),
    path('update/<int:pk>/', views.edit_portofolio_item, name='update_portofolio'),
    path('delete/<int:pk>/', views.delete_portofolio_item, name='delete_portofolio'),
]