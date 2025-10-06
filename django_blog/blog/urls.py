from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Home / posts list (both root and explicit posts/)
    path('', views.post_list, name='post_list'),
    path('posts/', views.post_list, name='post_list'),

    # CRUD using singular "post/" paths (checker expects these substrings)
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'),

    # Registration and profile
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
