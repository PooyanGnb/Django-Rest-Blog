import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime
from rest_framework import status

from accounts.models import User
from ..models import Post


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="admin@admin.com", password="a/@12341234", is_verified=True
    )
    return user


@pytest.mark.django_db
class TestPostApi:

    def test_get_post_response_200(self, api_client):
        url = reverse("blog:api-v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "test content",
            "status": True,
            "published_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_post_valid_data_response_201_status(self, api_client, common_user):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "test content",
            "status": True,
            "published_date": datetime.now(),
        }
        user = common_user
        # login user
        api_client.force_authenticate(user=user)
        # count the posts before the post creation
        initial_post_count = Post.objects.count()
        # post gets created
        response = api_client.post(url, data)
        # count the posts after the post creation
        new_post_count = Post.objects.count()
        # checks if the status code is 201 which means the post was created
        assert response.status_code == status.HTTP_201_CREATED
        # checks if post count has increased but 1
        assert new_post_count == initial_post_count + 1

    def test_create_post_invalid_data_response_400_status(
        self, api_client, common_user
    ):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "test content",
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
