from django.conf.urls import url
from raffle import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="raffle"),
    url(r'^participants/$', views.participants, name="participants"),
    url(r'^upload/$', views.upload_file, name="upload"),
    url(r'^privacy/$', views.privacy, name="privacy")
]
