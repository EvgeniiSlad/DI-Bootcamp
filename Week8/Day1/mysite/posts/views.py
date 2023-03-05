from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def some_text(request):
    """"Show text on sreen inside browser"""
    return HttpResponse('TEXT!')

def about(request):
    return HttpResponse('<h1> New TEXT!!!!!<h1>')

def posts(request):
    author = 'Evgenii'
    title = 'This is my first post'
    body = 'Text about my post etc.'

    context: dict = {'author': author, 'title': title, 'body': body}
    #context - data

    return render(request, 'posts.html',context)

def profile(request):
    
    context = {
        'name' : 'Evgenii',
        'age' : 23,
        'gender' : 'M',
        'hobbies' : ['Python','Django','Purim']
    }

    return render(request,'profile.html',context)