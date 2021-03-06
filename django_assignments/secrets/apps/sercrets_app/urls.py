from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^create$', views.create, name = 'create'),
    url(r'^like/(?P<secret_id>\d+)$', views.like, name = 'like'),
    url(r'^delete/(?P<secret_id>\d+)$', views.delete, name = 'delete'),
]
