from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^check$', views.check, name = 'check'),
    url(r'^show/(?P<course_id>)\d+', views.show_course, name = 'show_course'),
    url(r'^create$', views.create, name='create_course'),
    url(r'^delete/(?P<course_id>\d+)$', views.course_delete, name = 'delete_course'),
    url(r'^descripton/delete/(?P<descripton_id>\d+)$', views.descripton_delete),
    url(r'^user_course', views.user_to_course, name = 'add_user_to_course')
]
