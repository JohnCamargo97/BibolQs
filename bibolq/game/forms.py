from django import forms
from .models import Chapter, Verse


class VersePhraseSelect(forms.ModelForm):

    CHAPTERS = Chapter.objects.all().values_list('name', 'name')
    Chapter = forms.ChoiceField(widget=forms.Select, choices=CHAPTERS)
    IncompletePhrase = forms.CharField(max_length=1000)
    class Meta:
        model = Verse
        fields = ('Chapter', 'NumberVerse' ,'ContentVerse' ,'IncompletePhrase')
    #IncompleteVerse = forms.CharField(max_length=1000, label='Verso Incompleto', required=True)