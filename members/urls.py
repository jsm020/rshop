# urls.py
from django.urls import path
from .views import login_view, register_view,personal_cabinet

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('personal/', personal_cabinet, name='personal_cabinet'),


]
