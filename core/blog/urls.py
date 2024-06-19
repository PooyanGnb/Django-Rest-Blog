from django.urls import path, include
from django.views.generic import TemplateView
from . import views


app_name = 'blog'

urlpatterns = [
    # path("cbv/", views.IndexView.as_view(), name="cbv-index"),
    # path("linkedin/", views.RedirectToLinkedIn.as_view(), name="linkedin-redirect"),
    
    path("post/", views.PostList.as_view(), name="post-list"),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/<pk>/edit/", views.PostEditView.as_view(), name="post-edit"),
    path("post/<pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),

    path('api/v1/', include('blog.api.v1.urls'))
]