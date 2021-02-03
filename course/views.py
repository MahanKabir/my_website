from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from .forms import CourseForm
from .models import Course
# Create your views here.
from .serializers import CourseSerializer


def create(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    return redirect('dashboard')

def read(request):
    courses = Course.objects.all()
    return render(request, 'course_read.html', {'courses': courses})


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



@api_view(['POST'])
def api_create(request):
    if request.method == "POST":
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def api_read(request):
    if request.method == "GET":
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
@api_view(['PUT'])
def api_update(request, id):
    course = Course.objects.get(id=id)
    if request.method == "PUT":
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def api_delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return Response("successfully", status=HTTP_204_NO_CONTENT)
