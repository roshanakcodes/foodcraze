from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
# Create your views here.
def newuser(request):
    
         if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            email=request.POST['email']
            if User.objects.filter(username=username).exists():
                 return render(request, "userauth/newuser.html", {
                     "message": "Username already taken"
                 })
            else:
                try:
                     validate_password(password, user=User(username=username, email=email))
            
                except ValidationError as e:
                     error_message = " ".join(e.messages)
                     return render(request, "userauth/newuser.html", {"message": error_message})
                user = User.objects.create_user(username, email, password)
                #change_redirecttosign_up_usereverese()
                return render(request,"userauth/login.html",{
                  "message": "New user created",
                })

         else:
            return render(request,"userauth/newuser.html")

def login_view(request):
    if request.method=="POST":
      username = request.POST["username"]
      password = request.POST["password"]
      user=authenticate(request, username=username,password=password)
      if user is not None:
          login(request, user)
          return redirect('index')
      else:
          return render(request,"userauth/login.html",{
              "message": "Invalid credentials",
          })
    return render(request, "userauth/login.html")

def logout_view(request):
    logout(request)
    return render(request, "userauth/login.html", {
        "message": "Logged out"
    })

def index(request):
    if User.is_authenticated == "False":
         return render(request, "userauth/home.html")
    return redirect('fav')