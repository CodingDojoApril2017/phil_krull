from __future__ import unicode_literals
import re

from django.db import models

# Create your models here.
class EmailManager(models.Manager):
    def add_email(self, data):
        print data['email']
        errors = []
        if not data['email']:
            errors.append('Email field is required')
        if not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', data['email']):
            errors.append('Please enter a valid email')

        response = {}

        if not errors:
            new_email= self.create(email=data['email'])
            response['status'] = True
            response['success'] = new_email

        else:
            response['status'] = False
            response['errors'] = errors

        return response


class Email(models.Model):
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = EmailManager()
