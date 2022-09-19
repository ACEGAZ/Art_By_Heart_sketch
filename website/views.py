import pprint
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import (RegularCommissionForm, ReferenceSheetForm, CustomForm,
                    UploadArt)
from .models import AddArt, Comment


def index(request):
    """renders index page to index.html """
    return render(request, 'index.html')


def upload_art_view(request):
    """renders upload_art_view page to gallery.html
    and upload art form
    """
    if request.method == 'POST':
        upload_art_form = UploadArt(request.POST, request.FILES)
        if upload_art_form.is_valid():
            upload_art_form.save()
        return render(request, 'art_upload_success.html')
    upload_art_form = UploadArt()
    context = {'upload_art_form': upload_art_form}
    return render(request, 'admin_upload_art.html', context)


def display_artwork(request):
    """renders display_artwork forms to gallery.html"""
    pictures = AddArt.objects.all()
    comments = Comment.objects.all()
    context = {'pictures': pictures,
               'comments': comments}
    return render(request, 'gallery.html', context)


class AddCommentView(CreateView):
    """creates the AddCommentView view on gallery.html"""
    model = Comment
    template_name = 'add_comment.html'
    fields = ('name', 'body')
    success_url = '/add_comment_success/'

    def form_valid(self, form, **kwargs):
        form.instance.author = self.request.user
        post = AddArt.objects.get(pk=self.kwargs['pk'])
        form.instance.post = post
        return super().form_valid(form)


def add_comment_success(request):
    """renders add comment success page to add_comment_success.html """
    return render(request, 'add_comment_success.html')


class UpdateCommentView(UpdateView):
    """creates the UpdateCommentView view on gallery.html"""
    model = Comment
    template_name = 'update_comment.html'
    fields = ('name', 'body')
    success_url = '/gallery/'