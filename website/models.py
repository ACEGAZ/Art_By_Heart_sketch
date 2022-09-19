from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), 1, "Published")


class AddArt(models.Model):
    """add artwork to website """
    title = models.CharField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title


class RegularCommission(models.Model):
    """contact form for users to request regular commisions"""
    character_reference = models.CharField(max_length=100)
    character_owner = models.CharField(max_length=100)
    commission_type = models.CharField(max_length=100)
    type_option = models.CharField(max_length=100,)
    character_personality = models.CharField(max_length=100)
    pose = models.CharField(max_length=100)
    other_info = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email
