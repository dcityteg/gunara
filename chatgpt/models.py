from django.db import models

# Create your models here.

class Conversation(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField()
    model = models.TextField()
    title = models.TextField(blank=True, null=True)
    messages = models.JSONField()
    data = models.JSONField()
    datetime_field = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Conversation {self.id}"


