from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'sitemap/home.html')


def about(request):
    return HttpResponse('<h1>About site</h1>')


def contact(request):
    return HttpResponse('<h1>Contact Us</h1>')


def service(request):
    return HttpResponse('<h1>Our Services</h1>')