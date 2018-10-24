from django.shortcuts import render
#importataan Post olio jotta voidaan käyttää piste tarkoittaa että täältä kansioista
from .models import Post
from django.utils import timezone

#eli nyt tässä funktio post_list joka hakee requestilla html teidoston
#hei tässä nyt tarkkana. Nyt kun post_list.html niin kansiorakenne on blog/templates/post_list.html
def post_list(request):
    #eli tää post tekee quaryn viesteille ja antaa ne aikajärjestyksessä ulos
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #{'posts':post} antaa html noi oliot
    return render(request, 'post_list.html', {'posts':posts})
