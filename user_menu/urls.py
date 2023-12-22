from django.urls import path
from . import views
import django.contrib.auth.views
import apps.views


urlpatterns = [
    path('ordering/<int:good_id>', views.ordering, name='ordering'),

    path('ordering/login/', apps.views.user_login, name='ord_login'),

    path('ordering_success/', views.ordering_success, name='ordering_success'),

    path('', views.dashboard, name='dashboard'),

    path('comment/<int:good_id>', views.commenting, name='comment'),

    path('comment/login/', apps.views.user_login, name='com_login'),
]


