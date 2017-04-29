from django.shortcuts import render, redirect
from .models import Course
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
def index(request):
    context = {
        'courses':Course.objects.all(),
    }
    return render(request, 'first_app/index.html', context)

def create(request):
    if request.method == 'POST':
        course = Course.objects.create(name = request.POST['name'], description = request.POST['description'])
        print type(course)
        print type(model_to_dict(course))
        return JsonResponse(model_to_dict(course))
        # return redirect('main:index')
