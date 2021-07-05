from django.shortcuts import render,redirect

from .form import createuser,loginform
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method=='POST':
        fm=createuser(request.POST)
        if fm.is_valid():
            fm.save()
            messages.info(request,'Account is created successfully, Go to login')
    else:
        fm=createuser()
    return render(request,'account.html',{'form':fm})




def loginme(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print('Your are logged in')
            return redirect('/blog/profile/')
        else:
            messages.error(request,'Incorrect username or password!')

    fm=loginform()
    return render(request,'login.html',{'form':fm})