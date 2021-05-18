from django.contrib import admin

# Register your models here.
from urlShortener.shortener.models import UrlRedirect


@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('destiny', 'slug', 'createdIn', 'updated')
