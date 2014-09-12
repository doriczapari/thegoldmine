from django import forms
from .models import Post

from registration.forms import RegistrationForm



class PostForm(forms.ModelForm):
    
    link = forms.URLField(initial='http://')

    class Meta:
        model = Post
        fields = ('title', 'link', 'difficulty','text')