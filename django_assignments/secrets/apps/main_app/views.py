from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def register(request):
    response = User.objects.add_user(request.POST)
    if response['status']:
        request.session['user_id'] = response['new_user'].id
        request.session['user_fname'] = response['new_user'].first_name
        request.session['user_lname'] = response['new_user'].last_name
        return redirect('secrets:index')
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
        return redirect('secrets:index')
    else:
        for error in response['errors']:
            messages.error(request, error)
    return redirect('users:index')

def success(request):
    return render(request, 'main_app/success.html')

def logout(request):
    request.session.clear()
    return redirect('users:index')
