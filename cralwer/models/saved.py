from django.db import models

class Saved(models.Model):
    id = models.UUIDField(editable=False,primary_key=True)
    user_pk = models.ForeignKey("user",related_name='saved',on_delete=models.CASCADE, db_column="user_pk")
    saved_contents = models.TextField(blank=True,null=True)
    