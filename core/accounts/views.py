from django.http import HttpResponse, JsonResponse
from django.core.cache import cache
from .tasks import sendEmail
import requests


def test(request):
    # checks if the data is available in the cache
    if cache.get('test_delay_api') is None:
        # if it's not available, then make a request to fetch the data
        response = requests.get()
        # store the response in the cache and set the timeout to 60s
        cache.set('test_delay_api', response.json(), 60)
    return JsonResponse(cache.get('test_delay_api'))


def send_email(request):
    sendEmail.delay()
    return HttpResponse("email sent")