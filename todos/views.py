#django imports
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
#forms,models etc imports
from todos.forms import SignUpForm,LoginForm
from todos.models import Todo
# Create your views here.
def index(request):
    return render(request,"index.html")

class Login(View):
    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        response=""
        l=LoginForm(request.POST)
        if(l.is_valid()):
            user=l.cleaned_data
            print(user['username'])
            user=authenticate(username=user['username'],password=user['password'])
            if(user!=None):
                login(request,user,)
                response=redirect('/userpage')
            else:
                response=render(request,"login.html",{"error":"Wrong email or password"})
        else:
            response=render(request,"login.html",{"error":l.errors})
        return response

class SignUp(View):
    def get(self,request):
        return render(request,"signup.html")

    def post(self,request):
        s=SignUpForm(request.POST)
        response=None
        if(s.is_valid() and s.pass_match()):
            userdata=s.cleaned_data
            try:
                u=User.objects.get(email=userdata['email'])
                response=render(request,"signup.html",{"error":"Email is already in use"})
            except:
                u=User(username=userdata['username'],email=userdata['email'],password=userdata['password'])
                #u.save()
                #user=s.save(commit=False)
                u.set_password(userdata['password'])
                u.save()
                response=redirect('/login')
        else:
            if(s.pass_match() and s.is_valid()!=True):
                response=render(request,"signup.html",{"error":s.errors})
            elif(s.pass_match()!=True):
                response=render(request,"signup.html",{"error":"Passwords do not match"})
        return response
#@login_required
def userpage(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        #filter users todos
        userdata={"name":"test user","todos":[{"todo":"Learn Django"},{"todo":"Learn Flask"},{"todo":"Learn Dart"}]}
        return render(request,"userpage.html",{"userdata":userdata})

class Todos(View):
    @login_required
    def get(self,request,operation,todoid):
        return render(request,"todo.html")
    @login_required
    def post(self,request,operation,todoid):
        return render(request,"todo.html")


