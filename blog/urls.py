from django.urls import path
from . import views

#eli nytkun laitetu tuonne ekaan kansioon url.py että ohjaa tänne
#katsoo täältä view eli mennään views.py ja lataa sen
#nyt voidaan myös laittaa ns event tänne kun painaa sen post_detail niin täältä ohjaa viewiin
urlpatterns = [
    path('', views.post_list, name='post_list'),
    #Mitäs merkit tarkottaa'post/<int:pk>/'
    #"post/" url alkaa post alulla
    #<int:pk> django haluaa int arvon eli sen primary key mitä klikataan
    #/ kertoo ettö url loppuu
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    #Nyt yrl post/pk mitä editoitaan / edit 
    path('post/<int:pk>/edit/',views.post_edit, name = 'post_edit'),

]
