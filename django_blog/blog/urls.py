from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # this is correct — .views refers to blog/views.py

urlpatterns = [
    path('', views.post_list, name='post_list'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'),

    # Registration and profile
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
