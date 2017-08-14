from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^post/(?P<id>\d+)/$', views.PostView.as_view(), name="post"),
    url(r'^categories/$', views.CategoryView.as_view(), name="categories")
]
