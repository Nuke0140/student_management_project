from django.shortcuts import render,redirect


def BASE(request):
    return render(request,'base.html')


def Login(request):
    return render(request,'login.html')