from django.urls import path, include

app_name = 'forum'

urlpatterns = [
    path('api/', include('forum.api.urls', namespace = 'forum_api')),
]
