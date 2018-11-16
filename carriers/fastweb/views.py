from django.shortcuts import render
from django.shortcuts import redirect
from fastweb.lib.scraping import *
from fastweb.lib.datagestion import *
import fastweb.lib.utils as utils

# === Home view===
def home(request):
    """
    Get all offers stored in database and show it in home page
    :param request:
    :return: json plan offer
    """
    plans=models.Offers.objects.all()
    return render(request, 'innermain.html', context={"results": plans})

# === Buy Log===
def buylog(request):
    """
    Invoke UserInteraction objetct, fills data from user interface and hmtl page, store it in database

    :param request:
    :return: redirect to homepage
    """

    id_offer=request.GET['id']
    user=models.UserInteraction()
    user.id_offer=id_offer #offer name
    user.ip=utils.get_client_ip(request) #ip user address
    user.user_agent=request.META['HTTP_USER_AGENT'] #user agent
    user.save()

    return redirect('/') #redirect to homepage

# === Scraper view===
def scraper(request):
    """
    Invocke carrier class after is call the fucntion to call html code from url address, it is passed to Barutifulsoup object.
    Later is read html structure of page layaout and data are scrape from it.
    :param request:
    :return:
    """

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





