from django.views import generic
# from bakery.views import BuildableListView, BuildableDetailView
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


# class IndexView(BuildableListView):
#     model = models.Post
#     template_name = "index.html"
#     queryset = models.Post.objects.all()
#
#
# class PostView(BuildableDetailView):
#     model = models.Post
#     template_name = "post.html"
#     pk_url_kwarg = "id"
#     queryset = models.Post.objects.all()
#
#
# class CategoryView(BuildableListView):
#     model = models.Category
#     template_name = "categories.html"
#     queryset = models.Category.objects.all()
