from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.apps import apps

# Create your views here.
from django.contrib.auth.forms import UserCreationForm

from category.models import Category
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
def desktop(request):
    return render(request, 'admin/dashboard.html')



def perm(request):
    user = User.objects.get(id=1)
    content_type = ContentType.objects.get_for_model(Category)
    permission = Permission.objects.get(
        codename='change_category',
        content_type=content_type,
    )
    user.user_permissions.add(permission)
    return redirect('login')


def group_user(request):
    my_group = Group.objects.get(name='owner') 
    my_group.user_set.add(6)
    return redirect('login')

def create_group(request):
    new_group, created = Group.objects.get_or_create(name='asb')
    ct = ContentType.objects.get_for_model(Category)
    permission = Permission.objects.create(codename='add_category',
                                    name='Can add category',
                                    content_type=ct)
    new_group.permissions.add(permission)
    return redirect('login')

def user_manage(request):

    if request.method == "POST":
        new_group, created = Group.objects.get_or_create(name=request.POST['group'])
        ct = ContentType.objects.get_for_model(User)

        new_perm, permission = Permission.objects.get_or_create(
            codename=request.POST['codename'],
            name=request.POST['permname'],
            content_type=ct)

        if new_group:
            if new_perm:
                new_group.permissions.add(new_perm)
            else:
                new_group.permissions.add(permission)
        else:
            if new_perm:
                created.permissions.add(new_perm)
            else:                
                created.permissions.add(permission)


    app_models = [model.__name__ for model in apps.get_models()]
    return render(request, 'admin/manage.html', {'models': app_models})
