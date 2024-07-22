from django.test import SimpleTestCase, TestCase
from datetime import datetime

from ..forms import PostForm
from ..models import Category

# because of category, we use testcase instead of simpletestcase (access to dummy database) 
class TestPostForm(TestCase):

    def test_post_form_with_valid_data(self):
        category_obj = Category.objects.create(name='hello')
        form = PostForm(data={
            "title":"test",
            "content":"test content",
            "status":True,
            "category":category_obj,
            "published_date":datetime.now()
        })
        self.assertTrue(form.is_valid())

    def test_post_form_with_no_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())