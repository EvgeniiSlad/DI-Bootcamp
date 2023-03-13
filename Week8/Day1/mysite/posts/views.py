from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Addition

# Create your views here.
def some_text(request):
    """"Show text on sreen inside browser"""
    return HttpResponse('TEXT!')

def about(request):
    return HttpResponse('<h1> New TEXT!!!!!<h1>')

def posts(request):

    all_posts = Post.objects.all()
    context: dict = {'posts': all_posts}
    return render(request, 'posts.html',context)

def profile(request):
    
    context = {
        'name' : 'Evgenii',
        'age' : 23,
        'gender' : 'M',
        'hobbies' : ['Python','Django','Purim']
    }

    return render(request,'profile.html',context)


def post(request, id: int):
    post = Post.objects.get(id = id)
    addon = post.addition

    context = {'post': post,'addon': addon}

    return render(request,'post.html', context)

