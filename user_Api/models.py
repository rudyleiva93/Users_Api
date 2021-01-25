from django.db import models


class User(models.Model):
    gender = models.CharField(max_length=10)
    title = models.CharField(max_length=3)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
