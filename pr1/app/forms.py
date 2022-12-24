from django import forms
from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class ArticlesForm(ModelForm): 
    class Meta:
        model = Articles
        fields = ['title', 'full_text', 'date']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя человека'
            }),

            'full_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Причина смерти'
            }),

            'date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата смерти'
            })
        }

class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user