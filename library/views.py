from django.shortcuts import render


def index(request):
    context = {"title": "Main",
               }
    return render(request, 'index.html', context)

