from django.db import models
from django.contrib.auth.models import User

class DiaryModel(models.Model):
    date = models.DateField(unique=True)
    content = models.CharField()

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    age = models.IntegerField()
    instagram_id = models.CharField()
    bio = models.CharField()
