from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from backend.blog.sitemap import PostSitemap
from backend.pages.sitemap import PagesSitemap
from backend.forum.sitemap import TopicSitemap
from backend.courses.sitemap import CourseSitemap
from backend.reviews.sitemap import ReviewSitemap

sitemaps = {
    'blog': PostSitemap,
    'pages': PagesSitemap,
    'forum': TopicSitemap,
    'course': CourseSitemap,
    'review': ReviewSitemap,
}

urlpatterns = [
    path('djadmin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('accounts/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', include('backend.blog.urls')),
    path('course/', include('backend.courses.urls')),
    path('forum/', include('backend.forum.urls')),
    path('profile/', include('backend.profile.urls')),
    path('test/', include('backend.dc_tests.urls')),
    path('reviews/', include('backend.reviews.urls')),
    path('moderation/', include('backend.moderation.urls')),
    path('pay/', include('backend.pay.urls')),
    path('contact/', include('backend.contact.urls')),
    path('task/', include('backend.dc_task.urls')),
    path('friends/', include('backend.followers.urls')),
    path('groups/', include('backend.community.urls')),
    path('api/v2/', include('backend.api.v2.urls')),
    path('', include("backend.pages.urls")),
    path(
        'google1ca7c2f55e09214b.html/',
        lambda r: HttpResponse(
            "google-site-verification: google1ca7c2f55e09214b.html",
            mimetype="text/plain")
    ),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += DS_url
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
