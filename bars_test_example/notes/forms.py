from django import forms
from .models import Tag, Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['head_line', 'categories', 'body_text', 'favorite', 'tags']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
