from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from django.views import View
from .forms import ProjectForm, RatingForm
from django.http import HttpResponse
from .models import ProjectModel, RatingModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView


# Create your views here.
def add_category(request):
    if request.method == 'POST': 
        category_form = forms.CategoryForm(request.POST) 
        if category_form.is_valid(): 
            category_form.save() 
            return redirect('add_category') 
    
    else: 
        category_form = forms.CategoryForm()
    return render(request, 'add_category.html', {'form' : category_form})




@login_required
def addProject(request):
    if request.method == 'POST':
        project_form = forms.ProjectForm(request.POST)
        if project_form.is_valid():
            project_form.instance.user = request.user
            project_form.save()
            return redirect('add_project')  # Use the correct name here

    else:
        project_form = forms.ProjectForm()

    return render(request, 'projects/add_project.html', {'form': project_form})



def allProject(request):
    projects = ProjectModel.objects.all()
    return render(request, 'projects/all_project.html', {'project': projects})


# @method_decorator(login_required, name='dispatch')
# class AddProjectView(CreateView):
#     model = models.ProjectModel
#     form_class = forms.ProjectForm
#     template_name = 'add_project.html'
#     success_url = reverse_lazy('add_project')
    
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)





class DetailProjectView(DetailView):
    model = models.ProjectModel
    pk_url_kwarg = 'id'
    template_name = 'project_detail.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        project = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = project
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object 
        comments = project.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context





def ProjectRating(request, id):
    project = RatingModel.objects.get(pk=id)

    if request.method == 'POST':
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.user = request.user
            rating.project = project
            rating.save()
            return redirect('project_list')

    else:
        rating_form = RatingForm()

    return render(request, 'rate_project.html', {'project': project, 'rating_form': rating_form})