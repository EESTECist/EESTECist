from django.db import models


class Entry(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class TextFile(models.Model):
    text_file = models.FileField()
    hashtag = models.CharField(max_length=50)
