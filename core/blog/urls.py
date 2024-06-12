from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'blog'

urlpatterns = [
    path("cbv/", views.IndexView.as_view(), name="cbv-index"),
    path("post/", views.PostList.as_view(), name="post-list"),
    path("linkedin/", views.RedirectToLinkedIn.as_view(), name="linkedin-redirect"),
]