from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib import messages
# from .scrapper import scrapper
# from .selenium import selenium_func
# Create your views here.


def registerPage(request):
    if request.method =='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username.lower()
            user.save()
            return redirect('login')

        messages.error(request, form.errors)


    context = dict()
    return render(request, 'base/registration/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username').lower()
            password = request.POST.get('password')

            try:
                user = User.objects.get(username)

            except:
                messages.error(request, "User does not exist.")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            messages.error(request, "Invalid username or password.")
        messages.error(request,'Invalid username or password')

    context = dict()
    return render(request, 'base/registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def homePage(request):

    context = dict()
    return render(request,'base/home.html',context)

@login_required(login_url='login')
def showCases(request):
    if request.method == 'POST':
        data= request.POST
        print(data)
    context= dict()

    return render(request,'base/showCases.html',context)