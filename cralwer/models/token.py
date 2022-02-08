from django.db import models

class Token(models.Model):
    id = models.UUIDField(editable=False,primary_key=True)
    user_pk = models.ForeignKey("user",related_name='token', on_delete=models.CASCADE, db_column="user_pk")
    token = models.UUIDField(editable=True)