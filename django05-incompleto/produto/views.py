from django.shortcuts import render


def index(request):
    frase = "Esta frase está sendo exibida pela página index.html de produto."
    return render(request, 'produto/index.html', {'frase': frase})


def pagina1(request):
    frase = "Esta frase está sendo exibida pela página pagina1.html de produto."
    return render(request, 'produto/pagina1.html', {'frase': frase})


def pagina2(request):
    frase = "Esta frase está sendo exibida pela página pagina2.html de produto."
    return render(request, 'produto/pagina2.html', {'frase': frase})


