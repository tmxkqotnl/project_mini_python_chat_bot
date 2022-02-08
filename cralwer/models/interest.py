from django.db import models

class Interest(models.Model):
    id = models.UUIDField(editable=False,primary_key=True)