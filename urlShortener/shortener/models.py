from django.db import models

# Create your models here.


class UrlRedirect(models.Model):
    destiny = models.URLField(max_length=521)
    slug = models.SlugField(max_length=128, unique=True)
    createdIn = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'UrlRedirect para {self.destiny}'
