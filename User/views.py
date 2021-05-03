
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from User.models import  detail, modules
# Create your views here.
class information(forms.Form):
    name =forms.CharField(label="Enter your name :")
    surname =forms.CharField(label="Enter your surname :")
    idnumber =forms.IntegerField(label="Enter your idnumber :")
    email =forms.EmailField(label="Enter your email :")
    cellnumber =forms.IntegerField(label="Enter your cellnumber :")

class info_modules(forms.Form):
    preaching =forms.BooleanField(label="preaching")
    deliverance =forms.BooleanField(label="deliverance")
    ethics =forms.BooleanField(label="ethics")
    marriage =forms.BooleanField(label="marriage")

def index(request):

    if request.method == "POST":
        form =information(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            surname=form.cleaned_data["surname"]
            idnumber=form.cleaned_data["idnumber"]
            email=form.cleaned_data["email"]
            cellnumber=form.cleaned_data["cellnumber"]


            # semaka=user.name
            one= detail(name=name,surname=surname,idnumber=idnumber,email=email,cellnumber=cellnumber)
            one.save()
            return HttpResponseRedirect(reverse("module"))
        else:
            return render(request,"User/index",{
                "message" :"There was something wrong with your Info",
                "form": information()
            })
    elif not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("register"))
    else:
        return render(request,"User/index.html",{
            "form": information()
        })

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            password =form.cleaned_data.get('password')

            #semaka= user(username=username,password=password)
            #semaka.save()
            user = authenticate(request,username=username,password=password)
            login(request,user)
            
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"User/register.html",{
            "form": form,
            "message" : "Invalid credentials"
        })
    else:
        form =UserCreationForm()
        return render(request,"User/register.html",{
            "form": form
        })

def view_login(request):
    if request.method == "POST":
        username =request.POST["username"]
        password =request.POST["password"]
        user =authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"User/login.html",{
                "message":"Invalid credentials."
            })
    return render(request,"User/login.html")

def view_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def Choose_modl(request):
    if request.method == "POST":
        form =info_modules(request.POST)
        if form.is_valid():
            preaching =form.cleaned_data["preaching"]
            deliverance =form.cleaned_data["deliverance"]
            ethics=form.cleaned_data["ethics"]
            marriage=form.cleaned_data["marriage"]


            return render(request,"User/Choose_modl.html",{
            "form":info_modules(),
            "message": " Thanq you added your information succesfully"
            })
    else:
        return render(request,"User/Choose_modl.html",{
            "form":info_modules()
        })


