from django.shortcuts import render
from . import jsonConverter
from .forms import VersePhraseSelect
from .models import Verse, Chapter
from django.db.models import Count
from random import random, choice


def home(request):
    pk=choice(Verse.objects.values_list('pk', flat=True))
    #print(pk)
    Galatas = Verse.objects.get(pk=pk)
    #print(Verse.objects.all().count())
    chap = Chapter.objects.get(name="Galatas6")
    #Load = jsonConverter.chapter(jsonConverter.data)
    #currentchapt = Load.separateChapter()
    #print(currentchapt)
    #for verse, content in currentchapt.items():
    #    imp = Verse(chapter=chap, NumberVerse=verse, ContentVerse=content)       
    #    imp.save()
    format = 'shown'
    segment = ''
    formattedVerse = {}
    for ch in Galatas.ContentVerse:
        if ch == '{':  
            if segment != '':
                formattedVerse.update({segment:format})
                format = 'hidden'
                segment = ''

        elif ch == '}':
            formattedVerse.update({segment:format})
            format = 'shown'
            segment = ''      
        else:
            segment = segment + ch
    if segment != '':
        formattedVerse.update({segment:format})

    #print(formattedVerse)
    if request.method == "POST":
        Verseform = VersePhraseSelect(request.POST,instant=request.Verse )
    else:
        Verseform = VersePhraseSelect()

    context = {
        'vform' : Verseform,
        'verse': Galatas,
        'formattedVerse': formattedVerse
    }

    
    return render(request, 'home.html', context)