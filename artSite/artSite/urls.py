from django.urls import path
from artData import views

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('cust_form/', views.cust_form),
    path('cust_display', views.display, name = 'display'),
    path('dataEntry', views.dataEntry, name='dataEntry'),
    path('artist', views.artist, name = 'artist'),
    path('addArtist', views.addArtist, name = 'addArtist'),
    path('artwork', views.artwork, name = 'artwork'),
    path('artshow', views.artshow, name = 'artshow'),
    path('customer', views.customer, name = 'customer'),
    path('addCustomer', views.addCustomer, name = 'addCustomer'),
    path('collector', views.collector, name = 'collector'),
    path('buyer', views.buyer, name = 'buyer'),
    path('renter', views.renter, name = 'renter'),
    path('sale', views.sale, name = 'sale'),
    path('rent', views.rent, name = 'rent'),
    path('displayed', views.displayed, name = 'displayed'),
    path('sold', views.sold, name = 'sold'),
    path('rented', views.rented, name = 'rented')

    ]