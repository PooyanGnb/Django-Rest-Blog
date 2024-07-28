from django.urls import path, include
from . import views


app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("test", views.test, name="test"),
    path("send-email", views.send_email, name="send-email"),
    path("api/v1/", include("accounts.api.v1.urls")),
]
