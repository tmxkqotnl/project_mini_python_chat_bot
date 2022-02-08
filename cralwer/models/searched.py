from django.db import models

class Searched(models.Model):
    id = models.UUIDField(editable=False,primary_key=True)
    user_pk = models.ForeignKey("user",related_name='searched', on_delete=models.CASCADE, db_column="user_pk")
    query = models.CharField(max_length=150,blank=False,null=False)