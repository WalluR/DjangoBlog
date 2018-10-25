from django.shortcuts import render , get_object_or_404
#importataan Post olio jotta voidaan käyttää piste tarkoittaa että täältä kansioista
from .models import Post
from django.utils import timezone
from .forms import PostForm
#Ohjataan käyttäjiä eri mestoihin
from django.shortcuts import redirect

#eli nyt tässä funktio post_list joka hakee requestilla html teidoston
#hei tässä nyt tarkkana. Nyt kun post_list.html niin kansiorakenne on blog/templates/post_list.html
# ja kansiorakenne on aika saakelin tarkkaa!!! esim. error django.template.exceptions.TemplateDoesNotExist: blog/post_detail.html
#Johtuu siitä että kämmäät tiedostojen kanssa. eli tässä ei laiteta mitään blog/ alkua eteen tai kusee
def post_list(request):
    #eli tää post tekee quaryn viesteille ja antaa ne aikajärjestyksessä ulos
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #{'posts':post} antaa html noi oliot
    return render(request, 'post_list.html', {'posts':posts})

# auki kirjoitettuna parametrit request siis mikä tehdään ja pk
def post_detail(request,pk):
    # eli post = ota opbjekti jos ei ole palauta 404 error ( objekti Post, pk arvo = haluttu pk arvo)
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    #Eli tsekataan painettiinko nappia
    if request.method == "POST":
        #Ilmeisesti tuolla PostForm luokalla on request.POST metodi
        form = PostForm(request.POST)
        #Jos Form on validit
        if form.is_valid():
            #Otetaan ne kaikki jutut talteen
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #Eli heitetään käyttäjä sinne detailiin mikä just julkastiin. taas pk ettii sun oman postin
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def post_edit(request,pk):
    #Eli taas haetaan mikä postaus oli kyseessä
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        #instance asettaa sen haetun postauksen sinne formiin
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})
