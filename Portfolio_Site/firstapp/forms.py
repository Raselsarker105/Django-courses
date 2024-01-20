
from django import forms
from .models import ResumeModel, SkillModel, ContactModel

class ResumeForm(forms.ModelForm):
    class Meta:
        model = ResumeModel
        fields = ['file']



class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillModel
        fields = ['name', 'proficiency_level']



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=15, required=False)
    message = forms.CharField(widget=forms.Textarea)




