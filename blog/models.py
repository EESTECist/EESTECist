from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(blank=True)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey("Category", models.PROTECT)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
