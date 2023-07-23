# news/forms.py

from django import forms
from django.forms import ModelForm, ValidationError
from .models import NewsStory, Comment


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'image', 'pub_date', 'content']
        widgets = {
            'pub_date': forms.DateInput(
                format='%m/%d/%Y',
                attrs={
                    'class':'form-control',
                    'placeholder':'Select a date',
                    'type':'date'
                }
            ),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')


    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 10:
            raise ValidationError('Comment must be at least 10 characters long.')
        return text
