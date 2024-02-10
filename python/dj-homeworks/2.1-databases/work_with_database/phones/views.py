from django.shortcuts import render, redirect
from django.http import HttpResponse
from phones.models import Phone
# def index(request):
#     return redirect('catalog')
#
#
# def show_catalog(request):
#     template = 'catalog.html'
#     context = {}
#     return render(request, template, context)
#
#
# def show_product(request, slug):
#     template = 'product.html'
#     context = {}
#     return render(request, template, context)

def create_car(requests):
    phone = Phone(name = 'Iphone 12 mini', price = '60000')
    phone.save()
    return HttpResponse(f'Yeah, {phone.name}, {phone.model}')