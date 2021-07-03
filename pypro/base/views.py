from django.http import HttpResponse


# from django.shortcuts import render


# Create your views here (codigo aqui).

def home(request):
    return HttpResponse('Ola Django')