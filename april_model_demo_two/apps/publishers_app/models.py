from __future__ import unicode_literals

from django.db import models
from ..first_app.models import Book

# Create your models here.
class PublisherManager(models.Manager):
    def add_publisher(self, postData):
        if not len(postData['name']):
            # failed validations
            return (False, 'name is required!')
        else:
            # create our publisher
            publisher = self.create(name = postData['name'])
            return (True, publisher)

    def add_book_to_publisher(self, postData):
        print postData
        publisher = self.get(id = postData['publisher_id'])
        book = Book.run.get(id = postData['book_id'])
        publisher.books.add(book)

class Publisher(models.Model):
    name = models.CharField(max_length = 45)
    books = models.ManyToManyField(Book, related_name = 'published_by')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = PublisherManager()
