from django.http import HttpResponse, JsonResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from .tasks import sendEmail
import requests


@cache_page(60)
def test(request):
    response = requests.get()
    return JsonResponse(response.json())


# def test(request):
#     # checks if the data is available in the cache
#     if cache.get('test_delay_api') is None:
#         # if it's not available, then make a request to fetch the data
#         response = requests.get()
#         # store the response in the cache and set the timeout to 60s
#         cache.set('test_delay_api', response.json(), 60)
#     return JsonResponse(cache.get('test_delay_api'))


def send_email(request):
    sendEmail.delay()
    return HttpResponse("email sent")