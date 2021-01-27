from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from category.forms import CategoryForm
from .models import Category
from .serializers import CategorySerializer


def create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('read.cat')

    return render(request, 'category/create.html')

def read(request):
    pass
    # categories = Category.objects.all()
    # return render(request, 'category/read.html', {'categories': categories})

def dashboard_read(request):
    categories = Category.objects.all()
    return render(request, 'category/show.html', {'categories': categories})

def update(request):
    pass

def delete(request):
    pass



#------------------------------api

@api_view(['POST'])
def api_create(request):

    if request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_read(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

@api_view(['PUT'])
def api_update(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return Response(status=HTTP_204_NO_CONTENT)


