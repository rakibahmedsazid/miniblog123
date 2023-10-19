from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    password1= forms.CharField(label='Password',widget=forms.PasswordInput())
    password2 =forms.CharField(label='Conform Password (retype)',widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'username':"USERNAME",'first_name':'First Name','last_name':'Last Name','email':'Email'}
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','desc','img']
        labels = {'title':'Title','desc':'Descriptons','img':'Image'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'w-full'}),
            'desc':forms.Textarea(attrs={'class':'w-full'}),
        }