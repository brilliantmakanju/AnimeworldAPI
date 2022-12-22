from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    season = models.CharField(max_length=255)
    episode = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title


class Season(models.Model):
    thumbnail = models.ImageField()
    title = models.CharField(max_length=255)
    views = models.CharField(max_length=255)
    movieID = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name="movvieID", default='4')

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title


class Episode(models.Model):
    video = models.FileField()
    thumbnail = models.ImageField()
    title = models.CharField(max_length=255)
    views = models.CharField(max_length=255)
    seasonID = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="seaasonID", default='2')

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title
