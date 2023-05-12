
from django import forms
from .models import Comment

class CommentUpdateForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['content']   



class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
            