from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from music.models import Album


def index( request ):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_album': all_albums
    }
    return HttpResponse(template.render(context, request))


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    context = {
        'album': album
    }
    return render(request, 'music/details.html', context)
