from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm

from course.models import Course


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def dashboard(request):

    return render(request, 'dashboard.html')