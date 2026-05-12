from django.shortcuts import render
from . import jsonConverter
from .forms import VersePhraseSelect
from .models import Verse

def home(request):
    test = 'que{so}'
    Galatas1 = Verse.objects.filter(NumberVerse=24).all()
    if request.method == "POST":
        Verseform = VersePhraseSelect(request.POST,instant=request.Verse )
    else:
        Verseform = VersePhraseSelect()

    context = {
        'vform' : Verseform,
        'verses': Galatas1,
        'test':test
    }

    
    return render(request, 'home.html', context)