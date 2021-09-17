from django.shortcuts import render
from .forms import CreatPostForm
from .models import post
from blogger.models import blogger 
from django.http import HttpResponseRedirect
import datetime
# Create your views here.
def create_post(request, id):
    
    if request.method == "POST":
        writter = blogger.objects.get(id = id)
        print(datetime.datetime.now())
        new_post = post(date = datetime.datetime.now(), body=request.POST["body"], is_public = request.POST.get("private",0), blogger_id = writter)
        form = CreatPostForm(request.POST ,instance=new_post)
        form.save()
        return HttpResponseRedirect(f"/blogger/{id}/home")
        
    else:    
        form = CreatPostForm()
        return render(request, "posts/create_post.html",{"form":form})