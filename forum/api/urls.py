from django.urls import path
from .views import login, RegisterAPIView, ProfileAPIView, CategoryListAPIView, CategoryDetailAPIView, CreatePostAPIView, CategoryCreateAPIView, set_permission, NotificationListAPIView

app_name = 'forum_api'

urlpatterns = [
    path('login/', login, name = 'login'),
    path('register/', RegisterAPIView.as_view(), name = 'register'),
    path('profile/<int:pk>', ProfileAPIView.as_view(), name = 'profile'),
    path('', CategoryListAPIView.as_view(), name = 'categories'),
    path('category/<int:pk>', CategoryDetailAPIView.as_view(), name = 'category'),
    path('create_category/', CategoryCreateAPIView.as_view(), name = 'category_create'),
    path('create_post/', CreatePostAPIView.as_view(), name = 'create_post'),
    path('set_permission/', set_permission, name = 'set_permission'),
    path('get_notifications/<int:id>', NotificationListAPIView.as_view(), name = 'notification_list'),
]
