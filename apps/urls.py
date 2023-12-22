from django.urls import path
from . import views
import django.contrib.auth.views


urlpatterns = [
    path('', views.index, name='index'),
    path('bbr/', views.user),
    path('login/', django.contrib.auth.views.LoginView.as_view(), name='login'),
    path('logout/', django.contrib.auth.views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('add_goods/', views.add_goods, name='add_goods'),
    path('genre/<genre>', views.index, name='index-genre'),
    path('technique/<technique>', views.index, name='index-technique'),
    path('search/', views.index, name='index-search'),
    path('info/', views.info_board, name='info'),
    path('contact/', views.contact_form, name='contact'),
]

