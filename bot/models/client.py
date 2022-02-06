from django.db import models

class Client(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    user_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
