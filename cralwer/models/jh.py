from django.db import models

class JH(models.Model):
    id = models.UUIDField(editable=False,primary_key=True)