from django.urls import path
from django.views.generic import TemplateView
from .views import indexView, IndexView


urlpatterns = [
    path('', indexView, name="test"),
    path("cbv/", IndexView.as_view(), name="cbv-index"),
]