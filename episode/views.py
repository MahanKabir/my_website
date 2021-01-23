from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from episode.models import Episode
from course.models import Course
from .serializers import EpisodeSerializer



def create(request):
    pass


def read(request, id):
    episodes = Episode.objects.filter(course_id=id)
    return render(request, 'episode/read.html', {'episodes': episodes})


def update(request):
    pass


def delete(request):
    pass


# ==================================================
# ===============================================api
# ==================================================

@api_view(['POST'])
def api_create(request, id):
    course = Course.objects.get(id=id)

    if request.method == "POST":
        serializer = EpisodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(course_id=course.id)

            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_read(request, id):
    episode = Episode.objects.filter(course_id=id)
    if request.method == "GET":
        serializer = EpisodeSerializer(episode, many=True)
        return Response(serializer.data)

@api_view(['PUT'])
def api_update(request, id):
    episode = Episode.objects.get(id=id)
    if request.method == "PUT":
        serializer = EpisodeSerializer(episode, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_delete(request, id):
    episode = Episode.objects.get(id=id)
    if request.method == "DELETE":
        episode.delete()
        return Response("deleted")