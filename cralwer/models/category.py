from django.db import models

class Category(models.Model):
    id = models.UUIDField(editable=False,primary_key=True)
    large = models.CharField(editable=False,blank=False,null=False,max_length=22) 
    medium = models.CharField(editable=False,blank=False,null=False,max_length=22) 
    small = models.CharField(editable=False,blank=False,null=False,max_length=22) 
    