from django.shortcuts import render, HttpResponse

# Create your views here.
# this is the controller
def index(request):
    return HttpResponse('response from views.py')
