from django.shortcuts import render, redirect
from .models import Publisher
from django.contrib import messages

# Create your views here.
def create(request):
    print request.POST
    response = Publisher.objects.add_publisher(request.POST)
    print response
    if response[0] == False:
        messages.error(request, response[1])
    return redirect('book:index')

def publishers_has_books(request):
    print request.POST
    Publisher.objects.add_book_to_publisher(request.POST)

    return redirect('book:index')
