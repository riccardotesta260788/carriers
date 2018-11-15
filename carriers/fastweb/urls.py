from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from fastweb import views as mainview
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$',mainview.home,name="home"),
    url(r'scraper/$',mainview.scraper,name="scraper"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 ='fastweb.views.handler404'
handler500 ='fastweb.views.handler500'