from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from ..courses.models import Course, Description
# Create your views here.
def index(request):
    return render(request, 'loginReg/index.html')

def register(request):
    response = User.objects.add_user(request.POST)
    if response['status']:
        request.session['user_id'] = response['new_user'].id
        request.session['user_fname'] = response['new_user'].first_name
        request.session['user_lname'] = response['new_user'].last_name
        return redirect('courses:index')
    else:
        for error in response['errors']:
            messages.error(request, error)
    return redirect('users:index')

def login(request):
    response = User.objects.check_user(request.POST)
    if response['status']:
        request.session['user_id'] = response['loggedin_user'].id
        request.session['user_fname'] = response['loggedin_user'].first_name
        request.session['user_lname'] = response['loggedin_user'].last_name
        return redirect('courses:index')
    else:
        for error in response['errors']:
            messages.error(request, error)
    return redirect('users:index')

def success(request):
    anything = {
        'courses': Course.objects.all(),
        'users': User.objects.all(),
        'descriptons': Description.objects.all(),
    }
    return render(request, 'loginReg/success.html', anything)

def logout(request):
    request.session.clear()
    return redirect('users:index')
