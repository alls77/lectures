from time import sleep

from django.http import HttpResponse
from django.views.decorators.cache import cache_page


def index(request):
    text = 'Some text we want to return New One'
    sleep(10)
    return HttpResponse(text)


@cache_page(60 * 15)
def cached_view(request):
    text = 'This view is from cache'
    sleep(5)
    return HttpResponse(text)