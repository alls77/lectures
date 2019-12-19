from django.urls import path

from caching.views import index, cached_view
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', index),
    path('cached_view/', cached_view),
    # path('cached_view/',cache_page(60*15, cache='some_cache')(cached_view)) #cache in CACHES
]
