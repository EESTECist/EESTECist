from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('blog/', include("blog.urls")),
    path('', include("raffle.urls")),
    path('forum/', include('forum.urls', namespace = 'forum')),
]
