from django.db import models

# Create your models here.

class Language(models.Model):
    lang = models.CharField(max_length=1024,unique=True)

    def __str__(self):
        return self.lang

class MovieAlbum(models.Model):
    lang = models.ForeignKey(Language,on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

class Music(models.Model):
    movie_album_name = models.ForeignKey(MovieAlbum,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=1024)
    image = models.CharField(max_length=1024, )
    audio = models.CharField(max_length=1024)
    desc = models.CharField(max_length=999999, )
    date = models.DateField()