from django import forms
from .models import Tag, Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['pub_date']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
