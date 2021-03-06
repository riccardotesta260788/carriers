"""carriers URL Configuration
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')), #self generated documentation
    url(r'^admin/', admin.site.urls),
    #url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^', include('fastweb.urls')), #urls UI application endpoint
    url(r'^', include('fastweb.API.urls')),#urls API endpoint


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 ='fastweb.views.handler404'
handler500 ='fastweb.views.handler500'
