from django.db import models

class Searched(models.Model):
    id = models.UUIDField(editable=False,blank=False,null=False)
    user_id = models.ForeignKey("user", related_name="user", on_delete=models.CASCADE, db_column="user_id")
    query = models.CharField(max_length=150,blank=False,null=False)