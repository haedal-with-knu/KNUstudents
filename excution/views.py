from django.shortcuts import render
from .models import *

# Create your views here.

def category_all(request,category):
    if (category=='introduction'):
        category='국별 소개'
        posts = Post_introduction.objects.all()
    else:
        category='게시판'
        posts = Post_board.objects.all()
    return render(request, 'excution/category.html', {'posts': posts, 'category':category})


def post_detail(request, category, id):
    if category == 'board':
        cat = '게시판'
        post = Post_board.objects.get(category=category, id=id)
    else:
        cat = '국별 소개'
        post = Post_introduction.objects.get(category=category, id=id)
    return render(request, 'excution/detail.html', {'post' : post, 'cat':cat})

def 1(request):
    return render(request, 'excution/1.html')
def 2(request):
    return render(request, 'excution/2.html')
def 3(request):
    return render(request, 'excution/3.html')
def 4(request):
    return render(request, 'excution/4.html')
def 5(request):
    return render(request, 'excution/5.html')
def 6(request):
    return render(request, 'excution/6.html')

