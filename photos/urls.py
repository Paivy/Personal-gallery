from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home/',views.home, name='home'),
    path('show/', views.show, name='show'),
    path('search/', views.search, name='searchResults'),
    re_path('^location/(?P<locale>\w+)/', views.location, name='location'),
]

