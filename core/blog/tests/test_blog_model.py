from django.test import TestCase
from datetime import datetime

from ..models import Post, Category
from accounts.models import User, Profile


class TestPostModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email = "test@test.com",
            password  = "asdf34SFD4"
        )
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = "test name",
            last_name = "test last name",
            description = "test description",
        )

    def test_craete_post_with_valid_data(self):
        post = Post.objects.create(
            author = self.profile,
            title = "test",
            content = "test content",
            status = True,
            category = None,
            published_date = datetime.now()
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())