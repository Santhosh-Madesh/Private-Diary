from django.db import models

class DiaryModel(models.Model):
    date = models.DateField(unique=True)
    content = models.CharField()