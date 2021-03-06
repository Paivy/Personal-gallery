from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.posted_pics, name='Home'),
    path('big_image/<pic_id>', views.big_image, name="bigimage"),
    path('search/', views.search_results, name='search_results')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)