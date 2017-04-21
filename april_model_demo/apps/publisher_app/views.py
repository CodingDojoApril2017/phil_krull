from django.shortcuts import render, redirect
from .models import Publisher
from django.contrib import messages

# Create your views here.
def create(request):
    response = Publisher.objects.add_publisher(request.POST)
    if response[0]:
        print response[1]
    else:
        messages.error(request, response[1][0])
    return redirect('book:index')

def add_book_to_publisher(request):
    response = Publisher.objects.addBookToPublisher(request.POST)
    return redirect('book:index')
