from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import PlayList
from .forms import PlayListForm
from django.shortcuts import redirect


# def index(request):
# return HttpResponse("Please Enter a playlist ID")

def result(request, playlist_id):
    playlist = get_object_or_404(PlayList, pk=playlist_id)
    return render(request, 'result.html', {'playlist': playlist})


def new_playlist(request):
    if request.method == "POST":
        form = PlayListForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=True)
            return redirect('result', playlist_id=playlist.id)
    else:
        form = PlayListForm()
    return render(request, 'index.html', {'form': form})
