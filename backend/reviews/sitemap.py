from django.contrib.sitemaps import Sitemap

from .models import Review


class ReviewSitemap(Sitemap):

    def items(self):
        return Review.objects.filter(moderated=True)[:1]