from django.db import models

# Create your models here.
class Report(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('in_progress', 'In Progress'), ('completed', 'Completed')])
    file_path = models.CharField(max_length=255)