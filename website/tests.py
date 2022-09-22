from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.http import HttpRequest
from django.contrib.auth.models import User
from .views import (AddCommentView, UpdateCommentView, upload_art_view,
                    DeleteCommentView, index, display_artwork, commission_view,
                    add_comment_success)
from .forms import (UploadArt, RegularCommissionForm, ReferenceSheetForm,
                    CustomForm)
from .models import (AddArt, RegularCommission, ReferenceSheetCommission,
                     CustomCommissions, Comment)
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

    # def test_add_comment_is_resolved(self):
    #     url = reverse('add_comment', args=['comment1'])
    #     self.assertEqual(resolve(url).func.view_class, AddCommentView)

    # def test_update_comment_is_resolved(self):
    #     url = reverse('update_comment')
    #     self.assertEqual(resolve(url).func.view_class, UpdateCommentView)

    # def test_delete_comment_is_resolved(self):
    #     url = reverse('delete_comment')
    #     self.assertEqual(resolve(url).func.view_class, DeleteCommentView)


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


class TestModels(TestCase):

    def test_add_art_str(self):
        title = AddArt.objects.create(title='test title')
        self.assertAlmostEqual(str(title), 'test title')

    def test_regular_commission_str(self):
        email = RegularCommission.objects.create(email='test@gmail.com')
        self.assertAlmostEqual(str(email), 'test@gmail.com')

    def test_reference_sheet_commission_str(self):
        email = ReferenceSheetCommission.objects.create(email='test@gmail.com')
        self.assertAlmostEqual(str(email), 'test@gmail.com')

    def test_custom_commissions_str(self):
        email = CustomCommissions.objects.create(email='test@gmail.com')
        self.assertAlmostEqual(str(email), 'test@gmail.com')

    # def test_comment_str(self):
    #     author = User.objects(author='testuser')[0]
    #     name = Comment.objects.create(name='test name of post')
    #     body = Comment.objects.create(body='test body text')
    #     self.assertAlmostEqual(str(author, name, body), 'testuser', 'test name of post', 'test body text')


class TestViews(TestCase):

    def test_index_GET(self):
        client = Client()
        response = client.get(reverse(index))

        self.assertAlmostEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_upload_art_GET(self):
        client = Client()
        response = client.get(reverse(upload_art_view))

        self.assertAlmostEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_upload_art.html')

    def test_display_artwork_GET(self):
        client = Client()
        response = client.get(reverse(display_artwork))

        self.assertAlmostEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')

    # def test_add_comment_view_GET(self):
    #     client = Client()
    #     response = client.get(reverse(AddCommentView))

    #     self.assertAlmostEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'add_comment.html')

    def test_add_comment_success_GET(self):
        client = Client()
        response = client.get(reverse(add_comment_success))

        self.assertAlmostEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_comment_success.html')

    # def test_update_comment_view_GET(self):
    #     client = Client()
    #     response = client.get(reverse(UpdateCommentView))

    #     self.assertAlmostEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'update_comment.html')

    # def delete_comment_view_GET(self):
    #     client = Client()
    #     response = client.get(reverse(DeleteCommentView))

    #     self.assertAlmostEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'delete_comment.html')

    def test_commission_view_GET(self):
        client = Client()
        response = client.get(reverse(commission_view))

        self.assertAlmostEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'commissions.html')
