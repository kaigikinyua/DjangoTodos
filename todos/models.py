from django.db import models

# Create your models here.
class Todo(models.Model):
    todo=models.CharField(default="", max_length=50)
    deadline=models.DateField(auto_now=False, auto_now_add=False)
    owner=models.CharField(default="", max_length=50)
    state=models.BooleanField(default=False)
    priority=models.IntegerField()
