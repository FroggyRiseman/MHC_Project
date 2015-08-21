from django.shortcuts import render


def index(request):
    return render(request, 'chat/index.html')


def about(request):
    return render(request, 'chat/about.html')
