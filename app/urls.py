from django.urls import re_path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    re_path('^$',views.welcome, name="welcome"),
    re_path('register/', views.register, name ='register'),
    re_path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    re_path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    re_path('profiles/', views.profile, name='profile'),
    re_path('upload/', views.upload, name='upload'),
    re_path('business/', views.business, name = 'business'),
    re_path('news/', views.news, name="news")

]