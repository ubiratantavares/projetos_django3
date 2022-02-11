from django.shortcuts import render

def index(request):
    frase = "Esta frase está sendo exibida pela página index.html"
    return render(request, 'index.html', {'frase': frase})