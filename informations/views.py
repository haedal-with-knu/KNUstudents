from django.shortcuts import render
from .models import *

# Create your views here.

def category_all(request,category):
    if (category=='bylaw'):
        category='회칙'
        posts = Post_bylaw.objects.all()
    else:
        category='안건지/회의록'
        posts = Post_minutes.objects.all()
    return render(request, 'informations/category.html', {'posts': posts, 'category':category})





def post_detail(request, category, id):
    if category == 'minutes':
        cat = '안건지/회의록'
        post = Post_minutes.objects.get(category=category, id=id)
    else:
        cat = '회칙'
        post = Post_bylaw.objects.get(category=category, id=id)
    return render(request, 'informations/detail.html', {'post' : post, 'cat':cat})