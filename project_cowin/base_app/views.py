from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from . import forms
from . import models
# Create your views here.

def signup(request):
    form = forms.signup_form()
    d = models.District.objects.all()

    if request.method == 'POST':
        form = forms.signup_form(request.POST)
        if(form.is_valid()):
            form.save(commit='True')
            return HttpResponse('Done Succesfully !')
        return HttpResponse('Something went wrong!')
    else:
        return render(request,'test.html',context={'form':form})