
from django.shortcuts import render
from posts.models import post
from django.db.models import Q

# Create your views here.
def home(request, id):
    posts = post.objects.filter(Q(blogger_id = id) | Q(is_public ="1" )).order_by('-date')
    return render(request,'blogger/home.html', context={"posts": posts, "id":id})


