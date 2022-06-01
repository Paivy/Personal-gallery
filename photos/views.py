from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.




def home(request):
    return render(request, 'home.html')

def gallery(request):
    return render(request, 'all-photos/gallery.html')

def viewPhoto(request,pk):
    return render(request, 'all-photos/photo.html')

def addPhoto(request):
    return render(request, 'all-photos/add.html')