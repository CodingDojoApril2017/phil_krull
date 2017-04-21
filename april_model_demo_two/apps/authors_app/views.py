from django.shortcuts import render, redirect
from .models import Author

# Create your views here.
def create(request):
    # do validations
    if request.method == 'POST':
        Author.objects.create(name = request.POST['name'])

    return redirect('book:index')
