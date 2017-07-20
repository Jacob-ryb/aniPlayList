from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the playlist index.")

def results(request, playList_id):
    response = 'You are looking at %s. playlist'
    return response % playList_id
