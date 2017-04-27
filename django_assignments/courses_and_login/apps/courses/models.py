from __future__ import unicode_literals

from django.db import models
from ..loginReg.models import User

# Create your models here.
class CourseManager(models.Manager):
    def add_user_to_course(self, postData):
        user = User.objects.get(id = postData['user_id'])
        course = self.get(id = postData['course_id'])
        course.users.add(user)

class Description(models.Model):
    content = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    descripton = models.OneToOneField(Description)
    users = models.ManyToManyField(User, related_name = 'belongs_to')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = CourseManager()
