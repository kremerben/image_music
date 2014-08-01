from django.db import models

# Create your models here.


class Photo(models.Model):
    # owner = models.ForeignKey(User, related_name='owner')
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)

    def __unicode__(self):
        return self.image.name


class Song(models.Model):
    soundcloud_id = models.IntegerField()
    photo = models.ForeignKey(Photo, related_name='photo')
    title = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    stream_url = models.URLField(null=True, blank=True)
    download_url = models.URLField(null=True, blank=True)
    artwork_url = models.URLField(null=True, blank=True)
    waveform_url = models.URLField(null=True, blank=True)
    genre = models.CharField(max_length=200, null=True, blank=True)
    tag_list = models.CharField(max_length=500, null=True, blank=True)

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=200)
    photos = models.ManyToManyField(Photo, related_name='photo_tag')

    def __unicode__(self):
        return self.name
