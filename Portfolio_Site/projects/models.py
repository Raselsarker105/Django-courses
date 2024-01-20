from django.db import models
from django.contrib.auth.models import User
from .constants import PROJECT_TYPES

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class ProjectModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    screenshots = models.ImageField(upload_to='projects/media/uploads/', blank = True, null = True)
    technologies_used = models.CharField(max_length=255)
    project_url = models.URLField()
    category = models.CharField(max_length=50, choices=[('django', 'Django Projects'), ('android', 'Android Projects')])
    average_rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.title 
   
   
class Comment(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"Comments by {self.name}"
    

class RatingModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=zip(range(8), range(8)))
    average_rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return f"Rating for {self.project}"