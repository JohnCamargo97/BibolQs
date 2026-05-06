from django.db import models


class Chapter(models.Model):
    name = models.CharField(max_length=100)

class Verse(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    NumberVerse = models.SmallIntegerField(default=0)
    ContentVerse = models.CharField(max_length=1000)
    IncompletePhrase = models.CharField(max_length=1000, default="")