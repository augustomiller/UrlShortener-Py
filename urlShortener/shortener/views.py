from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from urlShortener.shortener.models import UrlRedirect


def page_redirect(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    return redirect(url_redirect.destiny)
