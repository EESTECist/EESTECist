from django.db import models
from django.contrib.auth.models import User

class Permission(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    is_mod = models.BooleanField(default = False)
    time_of_restriction = models.DateTimeField(blank = True, null = True)
    banned = models.BooleanField(default = False)
    can_create = models.BooleanField(default = False)
    can_vote = models.BooleanField(default = False)

    def __str__(self):
        return str(self.user)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'notification_user')
    _from = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'from_user')
    text = models.CharField(max_length = 280)
    date = models.DateTimeField(auto_now_add = True)


    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return str(self.text)

class Category(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'category_user')
    name = models.CharField(max_length = 140)
    date = models.DateTimeField(auto_now_add = True)
    follower = models.ManyToManyField(User)

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return str(self.name)

class Follower(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    follower = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.category)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    anon = models.BooleanField(default = False)
    date = models.DateTimeField(auto_now_add = True)
    text = models.CharField(max_length = 15 * 10**3)
    media = models.ImageField(blank = True, null = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    vote = models.IntegerField(default = 0)

    class Meta:
        ordering = ('-id', )
        get_latest_by = 'date'

    def __str__(self):
        return str(self.text)


    def save(self, *args, **kwargs):

        new_notification = Notification(user = self.category.user, _from = self.user, text = ' ')
        new_notification.save()

        super(Post, self).save(*args, **kwargs)
