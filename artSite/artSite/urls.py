from django.urls import path
from artData import views

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('queries', views.viewQueries, name='queries'),
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
    path('rented', views.rented, name = 'rented'),
    path('addArtwork', views.addArtwork, name = 'addArtwork'),
    path('addArtshow', views.addArtshow, name = 'addArtshow'),
    path('addCollector', views.addCollector, name = 'addCollector'),
    path('addBuyer', views.addBuyer, name = 'addBuyer'),
    path('addRenter', views.addRenter, name = 'addRenter'),
    path('addSale', views.addSale, name = 'addSale'),
    path('addRent', views.addRent, name = 'addRent'),
    path('query1',views.query1display, name='query1'),
    path('query2', views.query2display, name = 'query2'),
    path('query3', views.query3display, name = 'query3'),
    path('query4', views.query4display, name = 'query4'),
    path('query5', views.query5display, name = 'query5'),
    path('query6', views.query6display, name = 'query6')

    ]