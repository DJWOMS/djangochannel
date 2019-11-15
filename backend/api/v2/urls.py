from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Djangochannel API",
        default_version='v2',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="socanime@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('blog/', include('backend.api.v2.blog.urls')),
    path('profile/', include('backend.api.v2.profile.urls')),
    path('course/', include('backend.api.v2.courses.urls')),
    path('groups/', include('backend.api.v2.community.urls')),
    path('reviews/', include('backend.api.v2.reviews.urls')),
]
