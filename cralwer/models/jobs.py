from django.db import models

class Jobs(models.Model):
    id = models.UUIDField(editable=False,primary_key=True)