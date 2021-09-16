from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import signupForm,loginForm
from django.views import View
from .models import blogger
# Create your views here.
def home(request):
    return render(request,'blogger/home.html')

def signup(request):
    if request.method== "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/blogger/home")
        else:
            return HttpResponseRedirect("/blogger/signup")
    else:    
        form = signupForm()
        return render(request, "blogger/signup.html",{"form":form})

def login(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        user = blogger.objects.get(email=request.POST['email'])
        if user.password == request.POST['password']:
            return HttpResponseRedirect("/blogger/home")
        else:
            return HttpResponseRedirect('/blogger/login/')
    else:    
        form = loginForm()
        return render(request, "blogger/signup.html",{"form":form})