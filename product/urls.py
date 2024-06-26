from django.urls import path
from . import views

from .views import MahsulotList
urlpatterns = [
    path('',MahsulotList, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),



]
