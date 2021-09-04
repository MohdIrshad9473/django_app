import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Pk UUID? auto generated 

class Task (models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=50, null=False, )
    description = models.CharField(max_length=50,help_text="write description")
    create_date = models.DateTimeField(auto_now_add=True, editable=False,) 
    uuser = models.ForeignKey(
        User,
        related_name='task_user',
        null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
