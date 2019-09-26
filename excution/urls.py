from django.urls import path

from .views import *

app_name = 'excution'

urlpatterns= [
    path('<str:category>/', category_all, name='category_all'),
    path('<str:category>/detail/<int:id>', post_detail, name='post_detail'),
    path('introduction/nurse/', nurse, name='nurse'),
    path('introduction/ksd/', ksd, name='ksd'),
    path('introduction/engineering/', engineering, name='engineering'),
    path('introduction/scitech/', scitech, name='scitech'),
    path('introduction/teacher/', teacher, name='teacher'),
    path('introduction/lifesci/', lifesci, name='lifesci'),
    path('introduction/freemajor/', freemajor, name='freemajor'),
    path('introduction/administration/', administration, name='administration'),
]