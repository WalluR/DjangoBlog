from django.contrib import admin
from .models import Post
#eli siis importataan modelit postista mikä luotiin
# sitten meillä komenta että admin voi rekisteröidä postauksen
admin.site.register(Post)
