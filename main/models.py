from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.
class Tweet(models.Model):
    description = TextField();