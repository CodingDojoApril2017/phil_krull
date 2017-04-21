from django.shortcuts import render, redirect
from .models import Book
from django.contrib import messages
from ..authors_app.models import Author
from ..publishers_app.models import Publisher

# Create your views here.
def index(request):
    # print Book.objects.all()
    context = {
        'all_books': Book.run.all(),
        'all_authors': Author.objects.all(),
        'all_publishers': Publisher.objects.all()
    }
    return render(request, 'first_app/index.html', context)

def create(request):
    if request.method == 'POST':
        print request.POST
        response_from_models = Book.run.validateBook(request.POST)
        # book = Book.objects.create(title = request.POST['title'], author = request.POST['author'])
        print response_from_models
        # did not pass validations(boolean)
        if not response_from_models['status']:
            for model_error in response_from_models['errors']:
                messages.error(request, model_error)
        else:
            print response_from_models['book']


    return redirect('book:index')
