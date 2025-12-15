from django.db import models

# Create your models here.


class Genre(models.Model):
    gid = models.AutoField(primary_key=True)
    gname = models.CharField(max_length=50)

    def __str__(self):
        return self.gname


class Anime(models.Model):
    aid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="anime_images")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
