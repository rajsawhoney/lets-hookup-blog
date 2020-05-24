from django import forms
from .models import ModelFirst, ModelSecond


class ModelFirstForm(forms.ModelForm):

    class Meta:
        model = ModelFirst
        fields = ("name", "address")


class ModelSecondForm(forms.ModelForm):

    class Meta:
        model = ModelSecond
        fields = ("profession",)
