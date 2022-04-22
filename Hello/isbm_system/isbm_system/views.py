from ast import Return
from django.shortcuts import render,redirect,HttpResponse

from home.EmailBackend import EmailBackend

from django.contrib.auth import authenticate,logout,login


def BASE(request):
    return render(request,'base.html')


def Login(request):
    return render(request,'login.html')

def doLogin(request):
    if request.method =="POST":
        user = EmailBackend.authenticate(request,
                                       username=request.POST.get('email'),
                                       password=request.POST.get('password'),)
        
        if user !=None:
            login(request,user)
            user_type=user.user_type
            if user_type=="1":
                return HttpResponse("this is HOd pannel")
            elif user_type=="2": 
                return HttpResponse("this is staff panel")
            elif user_type=="3":
                return HttpResponse("this is student panel")
            else:
                #message
                return redirect('login')
        
        else:
            #message
            return redirect('login')
            