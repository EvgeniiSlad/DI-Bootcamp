from django.shortcuts import render
from .models import Category, Gif
from .forms import CategoryForm,GifForm
# Create your views here.

def homepage(request):

    if request.method == 'POST':
        print('DATA POST:', request.Post)
        form = GifForm(request.Post)
        form.save()

    gifs_all = Gif.objects.all()
    form = GifForm()
    context = {'gifs': gifs_all}

    data = request.GET
    like_id = data.get('LIKE')
    if like_id:
        add_like(int(like_id))

    return render(request, 'homepage.html', context)


def category(request,id: int):
    category_specific = Category.objects.get(id=id)
    category_gifs = category_specific.gifs.all()

    data = request.GET
    like_id = data.get('LIKE')
    if like_id:
        add_like(int(like_id))
    # dislike = request.GET.get('DISLIKE')
    # print(like_id)

    context = {'category': category_specific, 'gifs': category_gifs}

    return render(request, 'category.html', context)

def add_like(gif_id: int):
    gif = Gif.objects.get(id=gif_id)
    gif.likes += 1
    gif.save()



def categories(request):
    
    # Request methods
    # GET - getting data
    # POST - changing data

    if request.method == 'POST':
         print("DATA POST:", request.POST)
         form = CategoryForm(request.POST) # after data in form
         form.save()
    
    categories_all = Category.objects.all()
    form = CategoryForm() 
    context = {'categories': categories_all, 'form': form}

    return render(request, 'categories.html', context)
