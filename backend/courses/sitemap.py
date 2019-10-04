from django.contrib.sitemaps import Sitemap

from .models import Course


class CourseSitemap(Sitemap):

    def items(self):
        return Course.objects.filter(is_active=True)