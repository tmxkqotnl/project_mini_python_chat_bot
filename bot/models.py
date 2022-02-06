from django.db import models
from uuid import uuid4
class client(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    user_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=10)
    
    