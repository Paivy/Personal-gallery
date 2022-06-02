from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
import datetime as dt




def home(request):
    locations = Location.get_all()
    return render(request, 'home.html',{'locations':locations})

def gallery(request):
    return render(request, 'all-photos/gallery.html')

def show(request):
    images = Image.get_images()
    return render(request, 'show.html',{'images':images})

def search(request):
    title = Category.name
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_images(search_term)
        message = f"{search_term}"
        # print(searched_images)
        return render(request, 'search.html',{"message":message,"searched_images": searched_images,'title':title})
    


    else:
        message = "No term was searched "
        return render(request, 'search.html',{"message":message})

def location(request,locale):
    images = Image.filter_by_location(locale)
    return render(request, 'location.html', {'images':images})
