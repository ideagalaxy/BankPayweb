from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.first_page,name="fisrt_page"),
    path('log_in', views.login_page, name='log_in'),
    path('exchange', views.exchange_rate, name='exchange'),
    path('<int:pk>/',views.user_main_page,name="user_main_page"),
]