from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.first_page,name="fisrt_page"),
    path('log_in', views.login_page, name='log_in'),
    path('exchange', views.exchange_rate, name='exchange'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('exchange/detail', views.exchange_rate, name='exchange'),

    path('<int:pk>/',views.user_main_page,name="user_main_page"),
    path('change_money',views.change_money,name="change_money"),
    path('change_calculate',views.change_calculate,name="change_calculate"),

]