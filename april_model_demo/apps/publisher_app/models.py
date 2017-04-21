from __future__ import unicode_literals

from django.db import models
from ..first_app.models import Book

# Create your models here.

class PublisherManager(models.Manager):
    def add_publisher(self, postData):
        errors = []

        if not len(postData['name']):
            errors.append('name is required!')

        if errors:
            return (False, errors)
        else:
            publisher = self.create(name = postData['name'])
            return (True, publisher)

    def addBookToPublisher(self, postData):
        print postData
        publisher = self.get(id = postData['publisher_id'])
        book = Book.run.get(id = postData['book_id'])
        # publisher.books.add(book)
        book.published_by.add(publisher)

class Publisher(models.Model):
    name = models.CharField(max_length = 45)
    books = models.ManyToManyField(Book, related_name = 'published_by')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = PublisherManager()
