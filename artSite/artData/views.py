from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect
from .models import CustomerModel
from .forms import CustomerForm


# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def display(request):
    cust = CustomerModel.objects.all()
    return render(request, 'display.html', {'cust': cust})
def cust_form(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form':form}
    return render(request, 'customer.html', context)
