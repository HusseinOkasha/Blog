from django.shortcuts import render
from blogger.models import blogger
from .forms import SignupForm
from django.http import HttpResponseRedirect
# Create your views here.
def signup(request):
    if request.method== "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            id = blogger.objects.get(email = request.POST['email']).id
            return HttpResponseRedirect(f"/blogger/{id}/home")
        else:
            
            return HttpResponseRedirect("/signup")
    else:    
        form = SignupForm()
        return render(request, "signup/signup.html",{"form":form})
