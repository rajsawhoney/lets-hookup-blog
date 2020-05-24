from django.shortcuts import render
from .forms import ModelFirstForm, ModelSecondForm
# Create your views here.


def BiModelFormView(request):
    if request.method == "POST":
        firstform = ModelFirstForm(request.POST or None)
        secform = ModelSecondForm(request.POST or None)
        if firstform.is_valid() and secform.is_valid():
            person = firstform.save()
            secins = secform.save(commit=False)
            secins.person = person
            secins.save()
    else:
        firstform = ModelFirstForm()
        secform = ModelSecondForm()
    return render(request, 'checkform.html', {'form1': firstform, 'form2': secform})
