from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from .models import (
    CustomerModel
    # ArtistModel,
    # ArtWorkModel,
    # ArtShowModel
)
from .forms import CustomerForm


def display(request):
    cust = CustomerModel.objects.all()
    return render(request, 'display.html', {'cust': cust})
def cust_form(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form':form}
    return render(request, 'customer.html', context)

def homepage(request):
    return render(request, 'homepage.html')

def dataEntry(request):
    return render(request, 'dataEntry.html')

def artist(request):
    artists = ArtistModel.objects.all()
    return render(request, 'artist.html', {'artists': artists})

def addArtist(request):
    return render(request, 'addArtist.html')

def artwork(request):
    artworks = ArtworkModel.objects.all()
    return render(request, 'artwork.html', {'artworks': artworks})

def addArtwork(request):
    form = ArtworkForm(request.POST or None)
    if form.is_valid():
        form.save()
        # if ~(Artist.objects.get(id=form.cleaned_data['artistid'])):
        #    messages.error(request, 'artist does not exist')
        #    return HttpResponseRedirect('/addCustomer')
    context = {'form': form}
    return render(request, 'addArtwork.html', context)

def collector(request):
    return render(request, 'collector.html')

def customer(request):
    customers = CustomerModel.objects.all()
    return render(request, 'customer.html', {'customers': customers})

def addCustomer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        # if ~(Artist.objects.get(id=form.cleaned_data['artistid'])):
        #    messages.error(request, 'artist does not exist')
        #    return HttpResponseRedirect('/addCustomer')
    context = {'form': form}
    return render(request, 'addCustomer.html', context)

def artshow(request):
    artshows = ArtShowModel.objects.all()
    return render(request, 'artshow.html', {'artshows': artshows})

def buyer(request):
    return render(request, 'buyer.html')

def renter(request):
    return render(request, 'renter.html')

def rent(request):
    return render(request, 'rent.html')

def sale(request):
    return render(request, 'sale.html')

def displayed(request):
    return render(request, 'displayed.html')

def sold(request):
    return render(request, 'sold.html')

def rented(request):
    return render(request, 'rented.html')
