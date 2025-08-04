from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"traning/index.html")


def signup(request):
    return render(request,"traning/signup.html")

def signin(request):
    return render(request,"traning/signin.html")

def signout(request):
    pass