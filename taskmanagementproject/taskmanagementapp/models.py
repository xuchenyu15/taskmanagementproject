from django.db import models

# Create your models here.
class TaskManagementItem(models.Model):
    content = models.CharField(max_length=126)


