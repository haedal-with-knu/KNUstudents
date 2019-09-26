from django.shortcuts import render
from .models import *

# Create your views here.

def category_all(request,category):
    if (category=='introduction'):
        category='단위별 소개'
        posts = Post_introduction.objects.all()
    else:
        category='게시판'
        posts = Post_board.objects.all()
    return render(request, 'operation/category.html', {'posts': posts, 'category':category})





def post_detail(request, category, id):
    if category == 'board':
        cat = '게시판'
        post = Post_board.objects.get(category=category, id=id)
    else:
        cat = '단위별 소개'
        post = Post_introduction.objects.get(category=category, id=id)
    return render(request, 'operation/detail.html', {'post' : post, 'cat':cat})

def nurse(request):
    return render(request, 'operation/nurse.html')
def ksd(request):
    return render(request, 'operation/ksd.html')
def engineering(request):
    return render(request, 'operation/engineering.html')
def scitech(request):
    return render(request, 'operation/scitech.html')
def teacher(request):
    return render(request, 'operation/teacher.html')
def lifesci(request):
    return render(request, 'operation/lifesci.html')
def freemajor(request):
    return render(request, 'operation/freemajor.html')
def administration(request):
    return render(request, 'operation/administration.html')
def sangju(request):
    return render(request, 'operation/sangju.html')