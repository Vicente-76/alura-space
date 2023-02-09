from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia


def index(request):
    fotografias = Fotografia.objects.all()
    dados = {'cards': fotografias}
    return render(request, 'galeria/index.html', dados)


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    dados = {
        'fotografia': fotografia
    }
    return render(request, 'galeria/imagem.html', dados)


def buscar(request):
    pass
