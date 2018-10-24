from django.urls import path
from . import views

#eli nytkun laitetu tuonne ekaan kansioon url.py että ohjaa tänne
#katsoo täältä view eli mennään views.py ja lataa sen
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
