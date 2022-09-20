from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import AddCommentView, UpdateCommentView, DeleteCommentView, index, display_artwork, commission_view

# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_index_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_gallery_is_resolved(self):
        url = reverse('gallery')
        self.assertEquals(resolve(url).func, display_artwork)

    def test_commissions_is_resolved(self):
        url = reverse('commissions')
        self.assertEquals(resolve(url).func, commission_view)

    def test_add_comment_is_resolved(self):
        url = reverse('add_comment')
        self.assertEquals(resolve(url).func.view_class, AddCommentView)