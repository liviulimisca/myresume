from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    dictionar = {'key':"value"}
    return render(request, 'base.html', context=dictionar)


def resume(request):
    my_dictionary = {'insert_me': 'Hello there, Im from views.py', 'second': "Second Key"}
    return render(request, 'curriculum/resume.html', context=my_dictionary)
