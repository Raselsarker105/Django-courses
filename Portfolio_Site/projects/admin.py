from django.contrib import admin
from .models import ProjectModel, RatingModel, Comment
from . import models
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ['name', 'slug']
    
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(ProjectModel)
admin.site.register(RatingModel)
admin.site.register(Comment)
