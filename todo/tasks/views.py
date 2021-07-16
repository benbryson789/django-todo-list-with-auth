from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *
from django.contrib import messages 

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()



    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)
def myAccount(request):
    if request.user.is_authenticated == False:
        return redirect("/login")
    return render(request,"tasks/myaccount.html")
#dev/Admin@12345    
def registrationForm(request):
    context  ={}
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request,"Successfully created your account")
            return redirect("/login")
        else:
            messages.error(request,"You have entered a invalid data")    
    context['register_form'] = RegisterForm()
    return render(request,'tasks/register.html',context)        
def loginForm(request):
    context = {}
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('username')
            passwd = form.cleaned_data.get('password')
            user = authenticate(username=name,password=passwd)
            if user is not None:
                login(request,user)
                return redirect("/myaccount")
            else:
                messages.error(request,"You have entered invalid username and password")  
        else:
            messages.error(request,"You have entered invalid username and password")
        print("login-form-submit")
    context['login_form'] = AuthenticationForm()
    return render(request,"tasks/login.html",context)
def  logoutForm(request):
    logout(request)
    messages.info(request,"You have successfully logout from system")
    return redirect("/login")
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}

    return render(request, 'tasks/update_task.html',context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    context = {'item': item}
    return render(request, 'tasks/delete.html',context)

# def index(request):
#     return HttpResponse('Hello World')

