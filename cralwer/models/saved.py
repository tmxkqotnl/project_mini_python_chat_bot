from django.db import models

class Saved(models.Model):
    id = models.UUIDField(editable=False,blank=False,null=False)
    user_id = models.ForeignKey("user", related_name="user", on_delete=models.CASCADE, db_column="user_id")
    saved_contents = models.TextField(blank=True,null=True)
    