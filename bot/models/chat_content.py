from django.db import models

class ChatContent(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    user_pk = models.ForeignKey("Client",related_name="client",on_delete=models.CASCADE,db_column="user_pk")
    content = models.CharField(max_length=1000)
    static_url = models.CharField(max_length=1000,null=True,default=None)
    create_dt = models.DateTimeField()