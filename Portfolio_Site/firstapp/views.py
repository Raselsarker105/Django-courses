# views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import ResumeModel, SkillModel, ContactModel
from .forms import ResumeForm, SkillForm, ContactForm
from django.db.models import Avg


@login_required
def view_resume(request):
    resume = ResumeModel.objects.get_or_create(user=request.user)[0]
    return render(request, 'view_resume.html', {'resume': resume})

@login_required
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume, created = ResumeModel.objects.get_or_create(user=request.user)
            resume.file = form.cleaned_data['file']
            resume.save()
            return redirect('view_resume')
    else:
        form = ResumeForm()
    return render(request, 'upload_resume.html', {'form': form})




@login_required
def view_skills(request):
    skills = SkillModel.objects.filter(user=request.user)
    return render(request, 'view_skills.html', {'skills': skills})

@login_required
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            return redirect('view_skills')
    else:
        form = SkillForm()
    return render(request, 'add_skill.html', {'form': form})





@login_required
def contact_information(request):
    contact_info = ContactModel.objects.filter(user=request.user)
    return render(request, 'contact_info.html', {'contact_info': contact_info})


@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_no = form.cleaned_data['phone_no']
            message = form.cleaned_data['message']
            return redirect('contact_info')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})




# BLOG add korbo....



