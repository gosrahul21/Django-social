from django import forms

from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('description','image')



class CommentForm(forms.ModelForm):
    #list_pk = forms.IntegerField(widget=forms.HiddenInput)
    class Meta:
        model=Comment
        fields=['comment']