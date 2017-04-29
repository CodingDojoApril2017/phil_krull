from django.shortcuts import render
from django.http import JsonResponse
from .models import Course
from django.forms.models import model_to_dict

# Create your views here.
def index(request):
    print Course.objects.all(),
    context = {
        'courses':Course.objects.all(),
    }
    return render(request, 'first_app/index.html', context)

def create(request):
    if request.method == 'POST':
        course = Course.objects.create(name = request.POST['name'], description = request.POST['description'])
        print course
        return JsonResponse({'course': model_to_dict(course)})
