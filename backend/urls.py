from django.urls import path, include

urlpatterns = [
    # API
    path('', include('backend.api.v2.urls')),
]
