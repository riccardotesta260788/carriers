from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from fastweb.lib.scraping import *
from fastweb.lib.datagestion import *

# Create your views here.


def home(request):
    fast = Fastweb()
    html = fast.getHTML("http://www.fastweb.it")

    soup = fast.soup(html)
    soup = fast.fastStructure(soup)

    results = fast.getData(soup)

    return render(request, 'innermain.html', context={"results": results})

def scraper(request):
    #Creation scraping request to carrier's website
    fast = Fastweb()
    html = fast.getHTML("http://www.fastweb.it")
    soup = fast.soup(html)
    soup = fast.fastStructure(soup)

    results = fast.getData(soup) #JSON offer entries

    #Insert all scraped offer in database
    for entry in results:
        digest = CarriersData() # call specific class to manage carrier offer insert in database model
        digest.insert_off(entry,"Fastweb")

    return render(request, 'innermain.html', context={"results": results})



def handler404(request):
    return render(request, 'errors.html', status=404, context={"errore": '404',
                                                               "message":"Pagina non trovata"})

def handler500(request):
    return render(request, 'errors.html', status=500,context={"errore":'500',
                                                              "message":"Errore del server"})
