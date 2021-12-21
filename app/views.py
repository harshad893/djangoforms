from django.shortcuts import render

# Create your views here.
from app.forms import *

def djangoform(request):
    form_object=NameForm()
    d={'form_object':form_object}
    if request.method=='POST':
        FD=NameForm(request.POST)
        if FD.is_valid():
            name=FD.cleaned_data['name']
            

    return render(request,'djangoform.html',d)