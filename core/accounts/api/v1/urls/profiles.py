from django.urls import path, include
from .. import views

# app_name = 'api-v1'

urlpatterns = [
    # profile
    path("", views.ProfileApiView.as_view(), name="profile")
]
