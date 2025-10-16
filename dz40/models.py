from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)

class Page(models.Model):
    url = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
