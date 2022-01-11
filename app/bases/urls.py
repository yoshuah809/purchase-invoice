from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from bases.views import Home, HomeWithNoPrivileges

urlpatterns = [

    path('', Home.as_view(), name='home'),

    path('login/', auth_views.LoginView.as_view(template_name='bases/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='bases/login.html'), name='logout'),

    path('no_privileges/', HomeWithNoPrivileges.as_view(), name='no_privileges'),
]
