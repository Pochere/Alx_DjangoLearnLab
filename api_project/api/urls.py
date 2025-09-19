from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList
from .views import BookViewSet

# Creating a router and register BookViewSet
router = DefaultRouter()
router.register (r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),  # Includes all routes from the router (CRUD for BookViewSet)
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
