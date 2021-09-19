from django.forms.widgets import EmailInput
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import signupForm,loginForm
from django.views import View
from .models import blogger
from posts.models import post
from django.db.models import Q

# Create your views here.
def home(request, id):
    posts = post.objects.filter(Q(blogger_id = id) | Q(is_public ="1" )).order_by('-date')
    return render(request,'blogger/home.html', context={"posts": posts, "id":id})

def signup(request):
    if request.method== "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            id = blogger.objects.get(email = request.POST['email']).id
            return HttpResponseRedirect(f"/blogger/{id}/home")
        else:
            return HttpResponseRedirect("/blogger/signup")
    else:    
        form = signupForm()
        return render(request, "blogger/signup.html",{"form":form})

