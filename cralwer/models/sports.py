from django.db import models

class Sports(models.Model):
    id = models.UUIDField(editable=False,primary_key=True)