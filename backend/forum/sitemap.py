from django.contrib.sitemaps import Sitemap

from .models import Topic


class TopicSitemap(Sitemap):

    def items(self):
        return Topic.objects.filter(private=False)