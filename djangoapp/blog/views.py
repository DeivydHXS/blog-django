from django.shortcuts import render, get_object_or_404
from .models import Postagem, Categoria

def index(request):
    return render(request, 'blog/pages/home.html', {
        'categorias': Categoria.objects.all(),
        'postagens': Postagem.objects.all()[:5]
    })

def postagem(request, slug):
    return render(request, 'blog/pages/postagem.html', {
        'postagem': get_object_or_404(Postagem, slug=slug)
    })

def categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    return render(request, 'blog/pages/categoria.html', {
        'categoria': categoria,
        'postagens': Postagem.objects.filter(categoria=categoria)[:5]
    })