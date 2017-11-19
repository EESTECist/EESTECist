from django.conf.urls import url, include
from raffle import views

urlpatterns = [
    url(r'^$', views.IndexView, name="index"),
    url(r'^privacy$', views.privacy, name="privacy")
]
