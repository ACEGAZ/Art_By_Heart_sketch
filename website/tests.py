from django.test import TestCase
from django.urls import reverse, resolve
from django.http import HttpRequest
from django.contrib.auth.models import User
from .views import (AddCommentView, UpdateCommentView,
                    DeleteCommentView, index, display_artwork, commission_view)
from .forms import UploadArt, RegularCommissionForm, ReferenceSheetForm, CustomForm

# Create your tests here.


class TestUrls(TestCase):

    def test_index_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_gallery_is_resolved(self):
        url = reverse('gallery')
        self.assertEqual(resolve(url).func, display_artwork)

    def test_commissions_is_resolved(self):
        url = reverse('commissions')
        self.assertEqual(resolve(url).func, commission_view)

    def test_add_comment_is_resolved(self):
        url = reverse('add_comment')
        self.assertEqual(resolve(url).func.view_class, AddCommentView)

    def test_update_comment_is_resolved(self):
        url = reverse('update_comment')
        self.assertEqual(resolve(url).func.view_class, UpdateCommentView)

    def test_delete_comment_is_resolved(self):
        url = reverse('delete_comment')
        self.assertEqual(resolve(url).func.view_class, DeleteCommentView)


class TestForms(TestCase):

    def test_empty_upload_art_form(self):
        form = UploadArt()
        self.assertIn("title", form.fields)
        self.assertIn("featured_image", form.fields)

    def test_filled_upload_art_form(self):
        request = HttpRequest()
        request.POST = {
            "title": 'a title',
            "featured_image": "an image",
        }

        form = UploadArt(request.POST)
        form.save()

    def test_empty_regular_commission_form(self):
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
        form = ReferenceSheetForm()
        self.assertIn('character_reference', form.fields)
        self.assertIn('character_owner', form.fields)
        self.assertIn('design_changes', form.fields)
        self.assertIn('add_ons', form.fields)
        self.assertIn('other_info', form.fields)
        self.assertIn('email', form.fields)

    def test_filled_reference_sheet_form(self):

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

# class TestModels(TestCase):