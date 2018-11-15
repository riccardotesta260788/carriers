from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from fastweb.API.views import GetView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    #API
    url(r'api/onlineoffer/$',GetView.as_view(),name="onlineoffers"),

]
urlpatterns = format_suffix_patterns(urlpatterns)