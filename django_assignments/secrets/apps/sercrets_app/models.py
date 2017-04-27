from __future__ import unicode_literals
from ..main_app.models import User
from django.db import models

# Create your models here.
class Secret(models.Model):
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name = 'secret_creator')
    likes = models.ManyToManyField(User, related_name = 'user_likes')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
