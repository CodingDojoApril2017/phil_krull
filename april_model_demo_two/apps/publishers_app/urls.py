from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create$', views.create, name = 'create'),
    url(r'^bookToPub$', views.publishers_has_books, name = 'add_book_to_publisher')
]
