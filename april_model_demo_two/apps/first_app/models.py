from __future__ import unicode_literals

from django.db import models
from ..authors_app.models import Author

# Create your models here.

class BookManager(models.Manager):
    def validateBook(self, postData):
        validation_errors = []
        print postData

        if not len(postData['title']):
            validation_errors.append('title is required')
        # if not len(postData['author']):
        #     validation_errors.append('author is required')

        response_to_views = {}

        if validation_errors:
        # failed validations
            response_to_views['status'] = False
            response_to_views['errors'] = validation_errors
        else:
            # passed validations/ create the book
            author = Author.objects.get(id = postData['author_id'])
            book = self.create(title = postData['title'], author = author)
            response_to_views['status'] = True
            response_to_views['book'] = book

        return response_to_views

class Book(models.Model):
    title = models.CharField(max_length = 45)
    author = models.ForeignKey(Author, related_name = 'wrote')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    run = BookManager()
