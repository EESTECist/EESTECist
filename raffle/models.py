from django.db import models


class Entry(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    date = models.DateField(auto_now_add=True)


class TextFile(models.Model):
    text_file = models.FileField()
