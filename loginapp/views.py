from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def userlist(request):
    return render(request, 'userlist.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def logoutok(request):
    return render(request, 'logoutok.html')

def singupok(request):
    return render(request, 'signupok.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('mainpage')
        else:
            return render(request, 'loginpage.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'loginpage.html')

def signuppage(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            userform = UserCreationForm(request.POST)
            if userform.is_valid(): 
                user = userform.save()
                auth.login(request, user)
            return redirect('mainpage')
    return render(request, 'signuppage.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('mainpage')
    return render(request, 'signuppage.html')