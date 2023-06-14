from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=70)
    description=models.CharField(max_length=150)
    completed=models.BooleanField(default=False)