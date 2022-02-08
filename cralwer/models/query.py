from django.db import models

class Query(models.Model):
    id = models.UUIDField(editable=False,primary_key=True)
    user_pk = models.ForeignKey("user",related_name='query',on_delete=models.CASCADE, db_column="user_pk")
    large = models.TextField(blank=True,null=True)
    medium = models.TextField(blank=True,null=True)
    small = models.TextField(blank=True,null=True)