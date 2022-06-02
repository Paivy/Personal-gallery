from django.shortcuts import render
from django.http import HttpResponse
from .models import Picture


# Create your views here.

def posted_pics(request):
    pics = Picture.objects.all()

    return render(request, 'pic/index.html', {"pics": pics})


def search_results(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        name = Picture.objects.filter(name__contains=searched)
        return render(request, 'pic/search.html',{'searched':searched,'name':name,})
  

    else:
        message = "You have not searched for any picture"
        return render(request, 'pic/search.html', {"message": message})


  # if 'category' in request.GET and request.GET["category"]:
    #     searched_term = request.GET.get("category")
    #     searched_pictures = Picture.search_by_title(searched_term)
    #     message = f"{searched_term}"

    #     return render(request, 'pic/search.html', {"message": message, "pictures": searched_pictures})
def big_image(request,pic_id):
    image=Picture().objects.get(pk=pic_id)
    return render(request, 'pic/bigimage.html',{'image':image})

    