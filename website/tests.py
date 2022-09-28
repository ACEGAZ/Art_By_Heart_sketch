"""imprts from test, urls, http, user,
views, forms and models """
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.http import HttpRequest
from django.contrib.auth.models import User
from .views import (upload_art_view, index, display_artwork, commission_view,
                    add_comment_success)
from .forms import (UploadArt, RegularCommissionForm, ReferenceSheetForm,
                    CustomForm)
from .models import (AddArt, RegularCommission, ReferenceSheetCommission,
                     CustomCommissions)
# Create your tests here.


class TestUrls(TestCase):
    """tests index, gallery and commissions urls"""

    def test_index_is_resolved(self):
        """tests index url"""
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_gallery_is_resolved(self):
        """tests gallery url"""
        url = reverse('gallery')
        self.assertEqual(resolve(url).func, display_artwork)

    def test_commissions_is_resolved(self):
        """tests commissions url"""
        url = reverse('commissions')
        self.assertEqual(resolve(url).func, commission_view)


class TestForms(TestCase):
    """tests that upload art, regular commissions,
    reference sheet, commissions and customs forms fields exists
    and work when filled in """

    def test_empty_upload_art_form(self):
        """tests upload art fields exist """
        form = UploadArt()
        self.assertIn("title", form.fields)
        self.assertIn("featured_image", form.fields)

    def test_filled_upload_art_form(self):
        """tests upload art posts when filled in """
        request = HttpRequest()
        request.POST = {
            "title": 'a title',
            "featured_image": "an image",
        }

        form = UploadArt(request.POST)
        form.save()

    def test_empty_regular_commission_form(self):
        """tests regular commissions fields exist """
        form = RegularCommissionForm()
        self.assertIn('character_reference', form.fields)
        self.assertIn('character_owner', form.fields)
        self.assertIn('commission_type', form.fields)
        self.assertIn('type_option', form.fields)
        self.assertIn('character_personality', form.fields)
        self.assertIn('pose', form.fields)
        self.assertIn('other_info', form.fields)
        self.assertIn('email', form.fields)

    def test_filled_regular_commission_form(self):
        """tests regular commissions posts when filled in """
        request = HttpRequest()
        request.POST = {
            "character_reference": 'a character title',
            "character_owner": "a persons name",
            "commission_type": "full body",
            "type_option": "chibi",
            "character_personality": "crazy",
            "pose": "a pose description",
            "other_info": "anything to add",
            "email": "test@gmail.com",
        }

        form = RegularCommissionForm(request.POST)
        form.save()

    def test_empty_reference_sheet_form(self):
        """tests reference sheet fields exist """
        form = ReferenceSheetForm()
        self.assertIn('character_reference', form.fields)
        self.assertIn('character_owner', form.fields)
        self.assertIn('design_changes', form.fields)
        self.assertIn('add_ons', form.fields)
        self.assertIn('other_info', form.fields)
        self.assertIn('email', form.fields)

    def test_filled_reference_sheet_form(self):
        """tests reference sheet posts when filled in """
        request = HttpRequest()
        request.POST = {
            "character_reference": 'a character title',
            "character_owner": "a persons name",
            "design_changes": "a change",
            "add_ons": "something added on",
            "other_info": "any other info",
            "email": "test@gmail.com",
        }

        form = ReferenceSheetForm(request.POST)
        form.save()

    def test_empty_custom_form(self):
        """tests custom fields exist """
        form = CustomForm()
        self.assertIn('theme', form.fields)
        self.assertIn('colours', form.fields)
        self.assertIn('traits', form.fields)
        self.assertIn('gender', form.fields)
        self.assertIn('breed', form.fields)
        self.assertIn('accessories', form.fields)
        self.assertIn('other_info', form.fields)
        self.assertIn('email', form.fields)

    def test_filled_custom_form(self):
        """tests custom posts when filled in """
        request = HttpRequest()
        request.POST = {
            "theme": 'a character theme',
            "colours": "red",
            "traits": "a trait",
            "gender": "male/female",
            "breed": "pony",
            "accessories": "hairclip",
            "other_info": "some other info",
            "email": "test@gmail.com"
        }

        form = CustomForm(request.POST)
        form.save()


class TestModels(TestCase):
    """tests that add art, regular commissions, reference sheet
    and custom commissions models returns a string"""

    def test_add_art_str(self):
        """tests that add art returns a string"""
        title = AddArt.objects.create(title='test title')
        self.assertAlmostEqual(str(title), 'test title')

    def test_regular_commission_str(self):
        """tests that regular commission returns a string"""
        email = RegularCommission.objects.create(email='test@gmail.com')
        self.assertAlmostEqual(str(email), 'test@gmail.com')

    def test_reference_sheet_commission_str(self):
        """tests reference sheet comission returns a string"""
        email = ReferenceSheetCommission.objects.create(email='test@gmail.com')
        self.assertAlmostEqual(str(email), 'test@gmail.com')

    def test_custom_commissions_str(self):
        """tests that custom commissions returns a string"""
        email = CustomCommissions.objects.create(email='test@gmail.com')
        self.assertAlmostEqual(str(email), 'test@gmail.com')


class TestViews(TestCase):
    """tests that index, upload art, display artwork,
    add comment success, and commission
    views return a 200 respons on the correct template"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='jacob', email='soos@i.com', password='vvggtt')

    def test_index_get(self):
        """tests that index views return a 200 respons
        on the correct template"""
        client = Client()
        response = client.get(reverse(index))

        self.assertAlmostEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_upload_art_get(self):
        """tests that upload art views return a 200 respons
        on the correct template"""
        client = Client()
        response = client.get(reverse(upload_art_view))

        self.assertAlmostEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_upload_art.html')

    def test_display_artwork_get(self):
        """tests that display artwork views return a 200 respons
        on the correct template"""
        client = Client()
        response = client.get(reverse(display_artwork))

        self.assertAlmostEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')

    def test_add_comment_success_get(self):
        """tests that add comments success views return a 200 respons
        on the correct template"""
        client = Client()
        response = client.get(reverse(add_comment_success))

        self.assertAlmostEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_comment_success.html')

    def test_commission_view_get(self):
        """tests that commission views return a 200 respons
        on the correct template"""
        client = Client()
        response = client.get(reverse(commission_view))

        self.assertAlmostEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'commissions.html')
