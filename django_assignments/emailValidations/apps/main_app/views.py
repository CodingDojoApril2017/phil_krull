from django.shortcuts import render, redirect
from .models import Email
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'emails': Email.objects.all()
    }
    return render(request, 'main_app/index.html', context)

def create(request):
    if request.method == 'POST':
        res = Email.objects.add_email(request.POST)
        if res['status']:
            request.session['new_email'] = res['success'].email
        else:
            for error in res['errors']:
                messages.error(request, error)

    return redirect('index')
