from cgitb import html
import re
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate


def register(request):
    if request.method == "POST":
        #print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request,user)
            return redirect("home")
    #     else:
    #         for msg in form.error_messages:
    #             print(form.error_messages[msg])
    #             return render(request,'register.html',context={"form":form})
    #         #messages.success(request,'Account created successfully')
    # form = UserCreationForm()
    context = {'form':form}
    return render(request,'register.html', context)



def login(request):
    return render(request,'login.html')

def log_out(request):
    return render(request,'login.html')


def home(request):
    return render(request,'home.html')

