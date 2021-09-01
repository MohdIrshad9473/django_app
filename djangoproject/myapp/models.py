from django.db import models

# Create your models here.

class Task (models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True, editable=False,)
    updat_date = models.DateTimeField(auto_now=True, blank=True, null=True)
