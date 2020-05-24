from django import forms
from django.views.generic import FormView
from .models import Article
from tinymce.widgets import TinyMCE
from photos.models import Photo
from testapp.models import Category


class ArticleForm(forms.ModelForm):
    # images = forms.FileField(
    #     widget=forms.ClearableFileInput(attrs={'multiple': True}))
    assets = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=Photo.objects.all())

    class Meta:
        model = Article
        fields = ['category', 'title', 'content',
                  'ratings', 'thumbnail', 'assets', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Give your article a title...'}),
            'content': TinyMCE(attrs={'placeholder': 'Write your content here...'}),
            'ratings': forms.RadioSelect(attrs={'class': 'form-block', 'type': 'radio', }),
            'category': forms.SelectMultiple(attrs={'class': 'form-block', 'label': 'Choose the article category:'}),
            'assets': forms.SelectMultiple(attrs={'class': 'form-block', }),

        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description', 'cat_thumbnail', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Article Category Name Please...'}),
            'description': TinyMCE(attrs={'placeholder': 'Write a brief description about this here...'}),
        }


class ArticleEditForm(forms.ModelForm):
    # images = forms.FileField(
    #     widget=forms.ClearableFileInput(attrs={'multiple': True, }))
    assets = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=Photo.objects.all())

    class Meta:
        model = Article
        fields = ['category', 'title', 'content', 'assets']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title here...'}),
            'content': TinyMCE(attrs={'class': "mytinymce"}),
            'category': forms.SelectMultiple(attrs={'class': 'form-block', }),
            'assets': forms.SelectMultiple(attrs={'class': 'form-block', }),

        }
