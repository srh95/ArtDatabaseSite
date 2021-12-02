from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from .models import CustomerModel
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
    return render(request, 'artist.html')

def addArtist(request):
    return render(request, 'addArtist.html')

def artwork(request):
    artworks = ArtworkModel.objects.all()
    return render(request, 'artwork.html',{'artworks': artworks})

def collector(request):
    return render(request, 'collector.html')

def customer(request):
    customers = CustomerModel.objects.all()
    return render(request, 'customer.html',{'customers': customers})

def addCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            # if ~(Artist.objects.get(id=form.cleaned_data['artistid'])):
            #     messages.error(request, 'artist does not exist')
            #     return HttpResponseRedirect('/addCustomer')

            database = CustomerModel.objects.create(
                first_name = form.cleaned_data['firstname'],
                last_name = form.cleaned_data['lastname'],
                street_num = form.cleaned_data['streetnum'],
                street_name = form.cleaned_data['streetname'],
                city = form.cleaned_data['city'],
                state = form.cleaned_data['state'],
                zip_code = form.cleaned_data['zipocde'],
                preferred_style = form.cleaned_data['style'],
                preferred_medium = form.cleaned_data['medium'],
                phone_num = form.cleaned_data['phone'],
                artist_id = form.cleaned_data['artistid']
            )
            database.save()
            return HttpResponseRedirect('/customer')
    else:
        form = CustomerForm()

    return render(request, 'addCustomer.html', {'form': form})

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
