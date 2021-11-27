from django.urls import path
from artData import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('cust_form/', views.cust_form),
    path('cust_display', views.display, name = 'display'),
    ]