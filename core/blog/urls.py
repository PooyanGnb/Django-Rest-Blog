from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'blog'

urlpatterns = [
    # path("cbv/", views.IndexView.as_view(), name="cbv-index"),
    # path("linkedin/", views.RedirectToLinkedIn.as_view(), name="linkedin-redirect"),
    path("post/", views.PostList.as_view(), name="post-list"),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<pk>/", views.PostDetailView.as_view(), name="post-detail"),
]