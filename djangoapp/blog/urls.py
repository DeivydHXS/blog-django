from blog.views import *
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('postagem/<slug:slug>', postagem, name='postagem'),
    path('categoria/<slug:slug>', categoria, name='categoria'),
]
