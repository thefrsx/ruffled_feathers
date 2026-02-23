from django import forms
from .models import Edition, Story, Author


class EditionForm(forms.ModelForm):
    class Meta:
        model = Edition
        fields = ['title', 'number', 'thumb']


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'author', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 20, 'cols': 80})
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio', 'profile_picture']
