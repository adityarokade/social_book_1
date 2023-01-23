from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupFrom
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def sign_up(request):
    if request.method=="POST":
        fm =SignupFrom(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created successufully')
            fm.save()
    else:
        fm=SignupFrom()
        
        
    return render (request,'app1/register.html',{'form':fm})


def user_login(request):
    if request.method == "POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile/')
    else:
        fm=AuthenticationForm()
    return render(request,'app1/login.html',{'form':fm})


def user_profile(request):
    return render(request,'app1/profile.html')