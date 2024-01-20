from django import forms
from .models import ProjectModel, Category, RatingModel, Comment


class CategoryForm(forms.ModelForm):
    class Meta: 
        model = Category
        fields = '__all__'
        
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = '__all__'
        
        
class RatingForm(forms.ModelForm):
    class Meta:
        model = RatingModel
        fields = ['rating', 'average_rating']
        
        
class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'email', 'body']