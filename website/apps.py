"""imports from django.apps"""
from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    """default"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'website'
