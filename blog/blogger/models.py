from django.db import models

class blogger(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    username = models.CharField(max_length=128)
    email = models.EmailField()


