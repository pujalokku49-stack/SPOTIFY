from django.shortcuts import render
from .models import Song
# Create your views here.
def song_list(request):
    songs = Song.objects.all()
    return render(request,'song_list.html', {'songs': songs})
    
    