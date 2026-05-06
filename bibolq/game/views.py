from django.shortcuts import render
from . import jsonConverter
from .forms import VersePhraseSelect
# Create your views here.
def home(request):

    Galatas1 = jsonConverter.chapter(jsonConverter.data)
    if request.method == "POST":
        Verseform = VersePhraseSelect(request.POST,instant=request.Verse )
    else:
        Verseform = VersePhraseSelect()

    context = {
        'vform' : Verseform,
        'verses': Galatas1.separateChapter()
    }

    
    return render(request, 'home.html', context)