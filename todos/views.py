from django.shortcuts import render
from django.views import View
# Create your views here.
def index(request):
    return render(request,"index.html")

class Login(View):
    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        return render(request,"login.html")

class SignUp(View):
    def get(self,request):
        return render(request,"signup.html")
    def post(self,request):
        return render(request,"signup.html")

def userpage(request):
    return render(request,"userpage.html")

class Todos(View):
    def get(self,request,operation,todoid):
        return render(request,"todo.html")
    def post(self,request,operation,todoid):
        return render(request,"todo.html")
