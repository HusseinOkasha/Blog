from django.shortcuts import render
from .forms import LoginForm
from blogger.models import blogger
from django.http import HttpResponseRedirect
# Create your views here.
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        user = blogger.objects.get(email=request.POST['email'])
        if user.password == request.POST['password']:
            return HttpResponseRedirect(f"/blogger/{user.id}/home")
        else:
            return HttpResponseRedirect('/')
    else:    
        form = LoginForm()
        return render(request, "login/login.html",{"form":form})