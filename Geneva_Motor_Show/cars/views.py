from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from . import forms
from . import models
from django.views import View
from .models import Post
from django.http import HttpResponse
# Create your views here.
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

@login_required
def add_post(request):
    if request.method == 'POST': 
        post_form = forms.PostForm(request.POST) 
        if post_form.is_valid(): 
            # post_form.cleaned_data['author'] = request.user
            post_form.instance.author = request.user
            post_form.save() 
            return redirect('add_post') 
    
    else: 
        post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form' : post_form})


# Add Post using class Based view
@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        


class DetailCarView(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    
    
@method_decorator(login_required, name='dispatch')
class BuyCarView(DetailView):
    model = Post
    template_name = 'car_details.html'
    pk_url_kwarg = 'id'
    print("hghtyhy")

    def post(self, request, *args, **kwargs):
        car = self.get_object()
        print(car)

        if car.quantity > 0:
            car.quantity -= 1
            car.save()
    
            return redirect('profile')
        else:
            return redirect("car_out_of_stock")
        

       