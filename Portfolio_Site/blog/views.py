from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BlogPost
from .forms import BlogPostForm
# Create your views here.

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog_list.html'
    context_object_name = 'blog_posts'


def blog_detail(request, id):
    blog_post = BlogPost.objects.get(pk=id)
    return render(request, 'blog_detail.html', {'blog_post': blog_post})


from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import BlogPost
from .forms import BlogPostForm

@login_required
def BlogCreateView(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('homepage')
    else:
        form = BlogPostForm()

    return render(request, 'blog_form.html', {'form': form})

