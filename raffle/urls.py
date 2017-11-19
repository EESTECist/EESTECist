from django.conf.urls import url, include
from raffle import views

urlpatterns = [
    url(r'^$', views.IndexView, name="index"),
    url(r'^participants$', views.participants, name="participants"),
    url(r'^privacy$', views.privacy, name="privacy")
]
