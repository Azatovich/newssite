from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'newspaper/index.html')

def about(request):
    return render(request, 'newspaper/about.html')

def categories(request, catid):
    return HttpResponse(f"<h3> Статьи по категориям </h3><p>{catid}</p>")

def arhive(request, year):
    if int(year) > 2025:
        return redirect('home', permanent = False)

    return HttpResponse(f"<h1>Арихив по годам</h1><p>{year}</p>")

def pageNotFound(request, execption):
    return HttpResponseNotFound('<h1>Станица не найдена.</h1>')
