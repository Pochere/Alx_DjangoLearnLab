from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # this is correct — .views refers to blog/views.py

urlpatterns = [
    # blog posts
    path('', views.post_list, name='post_list'),
    path('posts/', views.post_list, name='post_list'), 

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'),

    # Registration and profile
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

# Blog CRUD URLs
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]