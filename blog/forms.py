from django import forms
from .models import Post


#Nyt luodaan uusi olio
#kerrotaan sille että tulee djangon from oliosta ja meidän Post oliosta joka luodaan model.py tiedostossa.
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
