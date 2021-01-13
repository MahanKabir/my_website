from django.shortcuts import render, redirect
from .forms import CourseForm
from .models import Course
# Create your views here.


def create(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    return redirect('dashboard')

def read(request):
    courses = Course.objects.all()
    return render(request, 'course/read.html', {'courses': courses})

def dashboard_read(request):
    courses = Course.objects.all()
    return render(request, 'course/show.html', {'courses': courses})

def update(request, id):
    course = Course.objects.get(id=id)
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    return render(request, 'course/update.html', {'course': course})

def delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('dashboard')
