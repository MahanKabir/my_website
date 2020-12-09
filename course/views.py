from django.shortcuts import render
from .forms import CourseForm
# Create your views here.


def create(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, 'course/create.html')

def read(request):
    pass

def update(request):
    pass

def delete(request):
    pass