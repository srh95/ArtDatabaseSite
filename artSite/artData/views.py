from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from .models import(
    CustomerModel,
    ArtistModel,
    ArtWorkModel,
    CollectorModel,
    ArtShowModel,
    BuyerModel,
    RenterModel,
    SaleModel,
    RentModel,
    query1)
from .forms import(
    CustomerForm,
    ArtistForm,
    ArtworkForm,
    ArtshowForm,
    CollectorForm,
    BuyerForm,
    RenterForm,
    SaleForm,
    RentForm)


def display(request):
    cust = CustomerModel.objects.all()
    return render(request, 'display.html', {'cust': cust})

def homepage(request):
    return render(request, 'homepage.html')

def dataEntry(request):
    return render(request, 'dataEntry.html')

def viewQueries(request):
    return render(request, 'queries.html')

def artist(request):
    artists = ArtistModel.objects.all()
    context = {'artists': artists}
    return render(request, 'artist.html', context)

def addArtist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ArtistForm()
    context = {'form': form}
    return render(request, 'addArtist.html', context)

def artwork(request):
    artworks = ArtWorkModel.objects.all()
    context = {'artworks': artworks}
    return render(request, 'artwork.html', context)

def addArtwork(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ArtworkForm()
    context = {'form': form}
    return render(request, 'addArtwork.html', context)

def collector(request):
    collectors = CollectorModel.objects.all()
    context = {'collectors': collectors}
    return render(request, 'collector.html', context)

def addCollector(request):
    if request.method == 'POST':
        form = CollectorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CollectorForm()
    context = {'form': form}
    return render(request, 'addCollector.html', context)

def customer(request):
    customers = CustomerModel.objects.all()
    context = {'customers': customers}
    return render(request, 'customer.html', context)

def addCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomerForm()
    context = {'form': form}
    return render(request, 'addCustomer.html', context)

def artshow(request):
    artshows = ArtShowModel.objects.all()
    context = {'artshows': artshows}
    return render(request, 'artshow.html', context)

def addArtshow(request):
    if request.method == 'POST':
        form = ArtshowForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ArtshowForm()
    context = {'form': form}
    return render(request, 'addArtshow.html', context)

def buyer(request):
    buyers = BuyerModel.objects.all()
    context = {'buyers': buyers}
    return render(request, 'buyer.html', context)

def addBuyer(request):
    if request.method == 'POST':
        form = BuyerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BuyerForm()
    context = {'form': form}
    return render(request, 'addBuyer.html', context)

def renter(request):
    renters = RenterModel.objects.all()
    context = {'renters': renters}
    return render(request, 'renter.html', context)

def addRenter(request):
    if request.method == 'POST':
        form = RenterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RenterForm()
    context = {'form': form}
    return render(request, 'addRenter.html', context)

def rent(request):
    rents = RentModel.objects.all()
    context = {'rents': rents}
    return render(request, 'rent.html', context)

def addRent(request):
    if request.method == 'POST':
        form = RentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RentForm()
    context = {'form': form}
    return render(request, 'addRent.html', context)

def sale(request):
    sales = SaleModel.objects.all()
    context = {'sales': sales}
    return render(request, 'sale.html', context)

def addSale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SaleForm()
    context = {'form': form}
    return render(request, 'addSale.html', context)

def displayed(request):
    context = {}
    return render(request, 'displayed.html', context)

def sold(request):
    context = {}
    return render(request, 'sold.html', context)

def rented(request):
    context = {}
    return render(request, 'rented.html', context)

def query1display(request):
    q1 = query1.objects.all()
    return render(request, 'query1.html', {'q1':q1})
