from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import PlayList


def index(request):
    return HttpResponse("Please Enter a playlist ID")


def result(request, playlist_id):
    playlist = get_object_or_404(PlayList, pk=playlist_id)
    print(playlist.mal_or_kitsu_link)
    return render(request, 'result.html', {'playlist': playlist})
