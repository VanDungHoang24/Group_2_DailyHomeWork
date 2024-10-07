from django.urls import path

from AppTwo import views
from django.conf.urls import include

urlpatterns = [
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('help/', views.help, name='help'),
    path('home/', views.home, name='home'),
]