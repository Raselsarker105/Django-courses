from django.db import models
from Categories.models import Category

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=100) 
    description = models.TextField(max_length=250)
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title