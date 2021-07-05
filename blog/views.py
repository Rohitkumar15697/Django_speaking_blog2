from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import blogpost

from .forms import Myblogform

import random
# Create your views here.

@login_required(login_url='login')
def profile(request):
    count=0
    if request.method=='POST':
        fm=Myblogform(request.POST)
        if fm.is_valid():
            topic=fm.cleaned_data['topic']
            title=fm.cleaned_data['title'].capitalize()
            post=fm.cleaned_data['post']
            obj=blogpost(topic=topic,title=title,post=post)
    
            obj.created_by=request.user  #this line fill the created_by column in models by current username automatically
            obj.save()
            return redirect('profile')
    else:
        fm=Myblogform()

    postdata=blogpost.objects.all().filter(created_by=request.user)
    print(list(postdata))
    
    count=len(postdata)
    
    fulldata=postdata[:1]  #Printing only current blog on the profile

    postdata=postdata[:15]  #Pring total 15 blogs title from first blog

    return render(request,'profile.html' ,{'data':postdata,'fulldata':fulldata,'count':count,'form':fm})



@login_required(login_url='login')
def logoutme(request):
    logout(request)
    return redirect('/')



