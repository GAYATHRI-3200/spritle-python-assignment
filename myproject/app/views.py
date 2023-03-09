from django.conf.global_settings import EMAIL_HOST_USER
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm
from django.contrib import  messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from django.core.mail import send_mail,EmailMessage
from .models import *

from django.conf import settings
from .forms import contactForm
from app import autoreply


from django.contrib.auth.models import User





def loginPage(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.info(request, 'Username or Password is Incorrect')

        return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for "+user)
                return redirect('login')

        context={'form': form}
        return render(request, 'register.html', context)


@login_required(login_url='login')    
def home(request):
  return render(request, 'home.html')

def Addition(num1,num2):
    result = int(num1) + int(num2)
    return result
 
def Subtract(num1,num2):
    result = int(num1) - int(num2)
    return result
 
def Divide(num1,num2):
    result = int(num1) // int(num2)
    return result
 
def Multiply(num1,num2):
    result = int(num1) * int(num2)
    return result
 

@login_required(login_url='login')
def main(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        if 'add' in request.POST:
            result = Addition(num1,num2)
            return render(request,'main.html',{'result':result})
        
        if 'sub' in request.POST:
            result = Subtract(num1,num2)
            return render(request,'main.html',{'result':result})
 
        if 'div' in request.POST:
            result = Divide(num1,num2)
            return render(request,'main.html',{'result':result})
 
        if 'mul' in request.POST:
            result = Multiply(num1,num2)
            return render(request,'main.html',{'result':result})
    return render(request, 'main.html')



def contact(request):
    title = "Contact"
    form = contactForm(request.POST or None) #form handling by view.
    confirmation = None

    if form.is_valid():
        user_name = form.cleaned_data['Username']
        user_message = form.cleaned_data['Message']
        emailsub = user_name + " tried contacting you on Dyslexia Prediction System."
        emailFrom = form.cleaned_data['UserEmail']
        emailmessage = '%s %s user email: %s' %(user_message, user_name, emailFrom)
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(emailsub, emailmessage, emailFrom, list(emailTo), fail_silently=True)
        #Autoreply.
        autoreply.autoreply(emailFrom)
        title = "Thanks."
        confirmation = "We will get right back to you."
        form = None

    context = {'title':title, 'form':form, 'confirmation':confirmation,}
    template = 'contact.html'
    return render(request,'contact.html',context)