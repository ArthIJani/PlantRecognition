from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, BlogPost


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
        
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ['date_created']
        fields = ['title', 'content', 'image']
