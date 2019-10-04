from django.contrib.sitemaps import Sitemap

from .models import Pages


class PagesSitemap(Sitemap):

    def items(self):
        return Pages.objects.filter(published=True)