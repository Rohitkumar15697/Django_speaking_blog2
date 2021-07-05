from django import forms
from .models import blogpost 


class Myblogform(forms.ModelForm):
    choices=(('None','Select you topic'),('Educational','Educational'),('Informational','Informational'),('Funny Thoughts/Jokes','Funny Thoughts/Jokes'),
    ('About Me','About Me'),('Sayri','Sayri'))
    topic=forms.ChoiceField(choices=choices)
    class Meta:
        model=blogpost
        fields=['topic','title','post']


