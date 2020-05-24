from django import forms
from .models import Comment
from tinymce.widgets import TinyMCE


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment_txt",)
        widgets = {
            'comment_txt': forms.Textarea(attrs={'class': 'form-control', 'rows': '2', 'cols': '20', 'placeholder': "Write your comment here...", 'label': ''})
        }

