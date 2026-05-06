from django import forms
from .models import Chapter, Verse


class VersePhraseSelect(forms.ModelForm):
    IncompletePhrase = forms.CharField(max_length=1000)
    class Meta:
        model = Verse
        fields = ('IncompletePhrase',)
    #IncompleteVerse = forms.CharField(max_length=1000, label='Verso Incompleto', required=True)