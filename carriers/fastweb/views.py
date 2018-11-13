from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'homepageNotLog.html', context={"message": "Home page"})


def login(request):
    return render(request, 'registration/login.html',context={})


def handler404(request):
    return render(request, 'errors.html', status=404, context={"errore": '404',
                                                               "message":"Pagina non trovata"})

def handler500(request):
    return render(request, 'errors.html', status=500,context={"errore":'500',
                                                              "message":"Errore del server"})
