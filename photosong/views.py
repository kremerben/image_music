import json
from django.shortcuts import render
import requests
# Create your views here.
from forms import *
from django.conf import settings
import soundcloud
from random import shuffle, sample, randint
client = soundcloud.Client(client_id=settings.SOUNDCLOUD_CLIENT_ID)


def home(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            photo_url = photo.image.url
            print photo_url
            #HARDCODED FOR DEMO PURPOSES
            if 'yosemite' in photo_url:
                urls = 'http://dev.kremerdesign.com/imagemusic/images/yosemite.jpg'
            elif 'spaceman' in photo_url:
                urls = 'http://dev.kremerdesign.com/imagemusic/images/spaceman.png'
            elif 'city' in photo_url:
                urls = 'http://dev.kremerdesign.com/imagemusic/images/city.jpg'
            else:
                urls = photo_url
            url = "http://rekognition.com/func/api/"
            payload = {
                "api_key": settings.REKOGNITION_API_KEY,
                "api_secret": settings.REKOGNITION_API_SECRET,
                "jobs": "scene_understanding_3",
                "urls": urls,
            }
            print payload
            r = requests.get(url, params=payload)
            # return render(request, "gallery/view_gallery.html", r.response)
            # print r
            # print r.text
            # print r.json()
            json_data = r.json()
            matches = json_data["scene_understanding"]["matches"]
            tags = []
            for tag in matches:
                name = tag['tag']
                current_tag, created = Tag.objects.get_or_create(name=name)
                current_tag.photos.add(photo)
                current_tag.save()
                tags.append(name)

            #FOR DEMO - ERROR CHECKING
            if len(tags) == 0:
                tags = ['power', 'lines', 'castle', 'awning', 'sunrise', 'downtown']

            tracks = []
            for tag in tags:
                 # find all sounds of buskers licensed under 'creative commons share alike'
                search_results = client.get('/tracks', q=tag, sharing='public', embeddable_by='all', streamable='true', )
                tracks += search_results

            #REMOVE EMPTY TRACKS BEFORE SENDING TO PAGE
            good_tracks = [i for i in tracks if hasattr(i, "id") and int(i.id) > 1]

            shuffle(good_tracks)
            album_tracks = sample(good_tracks, 10)

            #CHECKING FOR EMPTY FIELDS BEING RETURNED
            for track in album_tracks:
                try:
                    title = track.title
                except Exception, e:
                    title = "Untitled"
                try:
                    description = track.description
                except Exception, e:
                    description = ""
                try:
                    stream_url = track.stream_url
                except Exception, e:
                    stream_url = ""
                try:
                    download_url = track.download_url
                except Exception, e:
                    download_url = ""
                try:
                    artwork_url = track.artwork_url
                except Exception, e:
                    artwork_url = ""
                try:
                    waveform_url = track.waveform_url
                except Exception, e:
                    waveform_url = ""
                try:
                    genre = track.genre
                except Exception, e:
                    genre = ""
                try:
                    tag_list = track.tag_list
                except Exception, e:
                    tag_list = ""
                try:
                    sc_id = track.id
                except Exception, e:
                    sc_id = 999
                Song.objects.create(photo=photo,title=title,description=description,stream_url=stream_url,download_url=download_url,artwork_url=artwork_url,waveform_url=waveform_url,genre=genre,soundcloud_id=sc_id,tag_list=tag_list)

            data = {
                'tags': tags,
                'photo': photo,
                'album_tracks': album_tracks
            }

            return render(request, "home.html", data )
    else:
        form = PhotoForm()
    data = {"form": form}
    return render(request, "home.html", data)



#
def profile_update(request):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserForm(instance=user)
    data = {"user": request.user, "form": form}
    return render(request, "profile/profile_update.html", data)

