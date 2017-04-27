from django.shortcuts import render, redirect
from ..main_app.models import User
from .models import Secret
# Create your views here.
def index(request):
    context = {
        'secrets': Secret.objects.all(),
        'user': User.objects.get(id=request.session['user_id'])
    }

    return render(request, 'sercrets_app/index.html', context)

def create(request):
    user = User.objects.get(id=request.session['user_id'])
    Secret.objects.create(content=request.POST['secret'], user=user)
    return redirect('secrets:index')

def like(request, secret_id):
    user = User.objects.get(id=request.session['user_id'])
    secret = Secret.objects.get(id=secret_id)
    secret.likes.add(user)
    return redirect('secrets:index')

def delete(request, secret_id):
    Secret.objects.get(id=secret_id).delete()
    return redirect('secrets:index')
