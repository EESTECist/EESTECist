from django.urls import path
from .views import login, RegisterAPIView, ProfileAPIView, CategoryListAPIView, CategoryDetailAPIView, CreatePostAPIView, CategoryCreateAPIView 

app_name = 'forum_api'

urlpatterns = [
    path('login/', login, name = 'api_login'),
    path('register/', RegisterAPIView.as_view(), name = 'api_register'),
    path('profile/<int:pk>', ProfileAPIView.as_view(), name = 'api_profile'),
    path('', CategoryListAPIView.as_view(), name = 'api_categories'),
    path('category/<int:pk>', CategoryDetailAPIView.as_view(), name = 'api_category'),
    path('create_category/', CategoryCreateAPIView.as_view(), name = 'api_category_create'),
    path('create_post/', CreatePostAPIView.as_view(), name = 'api_create_post'),
]
