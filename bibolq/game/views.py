from django.shortcuts import render
from . import jsonConverter
# Create your views here.
def home(request):

    Galatas1 = jsonConverter.chapter(jsonConverter.data)
    return render(request, 'home.html', {'verses': Galatas1.separateChapter()})