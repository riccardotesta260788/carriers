from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from fastweb.lib.scraping import *
from fastweb.lib.datagestion import *
from rest_framework import serializers
from ..models import *

from rest_framework import generics
from .serializer import OfferSerializer



class GetView(generics.ListCreateAPIView):
    """This class defines the get behavior of our rest api."""
    queryset = Offers.objects.all()
    serializer_class = OfferSerializer

    def perform_get(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class Online():

    def getOnlineOffer(request):
        carrier = request.GET['carrier']
        # Creation scraping request to carrier's website

        if carrier == "Fastweb":
            url_carrier = "http://www.fastweb.it"
        else:
            results = {'Error': 'Carrier not Found'}
            return results

        fast = Fastweb()
        html = fast.getHTML(url_carrier)
        soup = fast.soup(html)
        soup = fast.fastStructure(soup)
        results = fast.getData(soup)  # JSON offer entries

        return results







