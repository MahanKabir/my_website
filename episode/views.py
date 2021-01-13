from django.shortcuts import render

# Create your views here.
from episode.models import Episode


def create(request):
    pass

def read(request, id):
    episodes = Episode.objects.filter(course_id=id)
    return render(request, 'episode/read.html', {'episodes': episodes})

def update(request):
    pass

def delete(request):
    pass