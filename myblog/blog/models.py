from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    author = models.OneToOneField(User, related_name='blogs')
    tags = models.TextField(null=True, blank=True)
    title = models.TextField(null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    ts_created = models.DateTimeField(auto_now=True)
    ts_updated = models.DateTimeField(auto_now=True, null=True, blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    full_name = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/')
    about = models.TextField()
    education = models.TextField()
    contact_info = models.TextField()
