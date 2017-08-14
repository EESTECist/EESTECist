from django.views import generic
from blog import models


class IndexView(generic.ListView):
    model = models.Post
    template_name = "index.html"


class PostView(generic.DetailView):
    model = models.Post
    template_name = "post.html"
    pk_url_kwarg = "id"


class CategoryView(generic.ListView):
    model = models.Category
    template_name = "categories.html"
