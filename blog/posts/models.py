from django.db import models
from blogger.models import blogger

class post(models.Model):
    date = models.DateTimeField()
    body = models.TextField(max_length=1000)
    is_public = models.BooleanField(default=False, blank=True)
    blogger_id = models.ForeignKey(blogger, on_delete=models.CASCADE)
