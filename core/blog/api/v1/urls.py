from django.urls import path, include
from . import views


app_name = 'api-v1'

urlpatterns = [
    path("post/", views.postList, name="post-list"),
    path("post/<id", views.postDelete, name="post-delete"),
]