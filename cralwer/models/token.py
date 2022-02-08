from uuid import UUID
from django.db import models

class Token(models.Model):
    token_serial = models.UUIDField(editable=False,primary_key=True)