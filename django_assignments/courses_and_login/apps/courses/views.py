from django.shortcuts import render, redirect
from .models import Course, Description
from django.contrib import messages
from ..loginReg.models import User

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        anything = {
            'courses': Course.objects.all(),
            'users': User.objects.all(),
            'descriptons': Description.objects.all(),
        }
        return render(request, 'courses/index.html', anything)
    else:
        messages.error(request, 'Must be logged in to continue!')
        return redirect('users:index')

def create(request):
    descripton = Description.objects.create(content=request.POST['content'])
    Course.objects.create(name = request.POST['name'], descripton = descripton)
    return redirect('courses:index')

def course_delete(request, course_id):
    Course.objects.filter(descripton_id = course_id).delete()
    return redirect('courses:index')

def descripton_delete(request, descripton_id):
    Description.objects.filter(id = descripton_id).delete()
    return redirect('courses:index')

def show_course(request, course_id):
    print 'in show'
    context = {
        'course': course_id
    }
    return render(request, 'courses/show.html', context)

def check(request):
    print 'in check'
    return redirect('courses:show_course', course_id=2)

def user_to_course(request):
    if request.method == 'POST':
        print request.POST
        Course.objects.add_user_to_course(request.POST)
    return redirect('courses:index')
