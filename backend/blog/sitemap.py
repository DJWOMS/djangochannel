from django.contrib.sitemaps import Sitemap

from .models import Post


class PostSitemap(Sitemap):

    def items(self):
        return Post.objects.filter(published=True)