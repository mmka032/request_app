from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'request/index.html')

def detail(request):
    return HttpResponse('Hello World')