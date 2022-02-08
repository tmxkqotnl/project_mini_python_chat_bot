from django.db import models

class User(models.Model):
    id = models.UUIDField(editable=False,primary_key=True)
    user_id = models.CharField(max_length=100,blank=False,null=False)
    password = models.CharField(max_length=100,blank=False,null=False)
    