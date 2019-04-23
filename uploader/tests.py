from django.test import TestCase
from uploader.models import Post

class PostTestCase(TestCase):

    def test_post_title(self):
        """The correct title is returned after a user uploads an image"""
        testImage = Post.objects.create(title="test image!")
        self.assertEqual(testImage.__str__(), 'test image!')