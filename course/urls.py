
from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create.course'), #localhost:8000/course/create
    path('read', views.read, name='read.course'), #localhost:8000/course/read
    path('dashboard/read', views.dashboard_read, name='dashboard.course'), #localhost:8000/course/dashboard/read
    path('update/<int:id>', views.update, name='update.course'), #localhost:8000/course/update/id
    path('delete/<int:id>', views.delete, name='delete.course'), #localhost:8000/course/delete/id

    path('api/v1/create', views.api_create, name="api.create.course"),
    path('api/v1/read', views.api_read, name="api.read.course"),
    path('api/v1/update/<int:id>', views.api_update, name="api.update.course"),
    path('api/v1/delete/<int:id>', views.api_delete, name="api.delete.course"),
]