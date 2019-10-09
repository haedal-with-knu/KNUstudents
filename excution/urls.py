from django.urls import path

from .views import *

app_name = 'excution'

urlpatterns= [
    path('<str:category>/', category_all, name='category_all'),
    path('<str:category>/detail/<int:id>', post_detail, name='post_detail'),
    path('excution/#', 1, name='#'),
    path('excution/#', 2, name='#'),
    path('excution/#', 3, name='#'),
    path('excution/#', 4, name='#'),
    path('excution/#', 5, name='#'),
    path('excution/#', 6, name='#'),
    path('excution/#', 7, name='#'),

]