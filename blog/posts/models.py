from django.db import models

class post(models.Model):
    date = models.DateTimeField()
    body = models.TextField(max_length=1000)
    is_public = models.BooleanField()
    blogger_username = models.CharField(max_length=128)
