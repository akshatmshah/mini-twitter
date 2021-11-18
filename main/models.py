from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Tweet(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True, null = True)
    tags = TaggableManager()

    class Meta:
        app_label = "main"

    def __str__(self):
        return self.description


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)

    class Meta:
        app_label = "main"

    def __str__(self):
        return self.user.username