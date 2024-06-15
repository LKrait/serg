from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'sitemap/home.html')


def about(request):

    return render(request, 'sitemap/about.html')


def contact(request):
    return render(request, 'sitemap/contacts.html')


def service(request):
    return render(request, 'sitemap/service.html')

