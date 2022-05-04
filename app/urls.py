from django.urls import path

from . import views

urlpatterns = [
    path('', views.brand_list, name='brands'),
    path('add_brand/', views.add_brand, name='add_brand'),
    path('edit_brand/<int:pk>/', views.edit_brand, name='edit_brand'),
    path('delete/<int:pk>/', views.delete_brand, name='delete_brand'),
    
]