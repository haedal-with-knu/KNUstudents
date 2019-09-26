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

def nurse(request):
    return render(request, 'excution/nurse.html')
def ksd(request):
    return render(request, 'excution/ksd.html')
def engineering(request):
    return render(request, 'excution/engineering.html')
def scitech(request):
    return render(request, 'excution/scitech.html')
def teacher(request):
    return render(request, 'excution/teacher.html')
def lifesci(request):
    return render(request, 'excution/lifesci.html')
def freemajor(request):
    return render(request, 'excution/freemajor.html')
def administration(request):
    return render(request, 'excution/administration.html')

