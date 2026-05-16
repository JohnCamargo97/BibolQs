from django.db import models


class Chapter(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Verse(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    NumberVerse = models.SmallIntegerField(default=0)
    ContentVerse = models.CharField(max_length=1000)
    #IncompletePhrase = models.CharField(max_length=1000, default="")

    def __str__(self):
        chapter = str(self.chapter)
        NumberVerse = str(self.NumberVerse)
        return chapter + ":" +NumberVerse