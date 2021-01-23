from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:id>', views.create, name="create.episode"),#localhost:8000/episode/create/id
    path('read/<int:id>', views.read, name="read.episode"),#localhost:8000/episode/read/id
    path('update/<int:id>', views.update, name="update.episode"),#localhost:8000/episode/update/id
    path('delete/<int:id>', views.delete, name="delete.episode"),#localhost:8000/episode/delete/id

    path('api/v1/create/<int:id>', views.api_create, name="api.create.episode"),
    path('api/v1/read/<int:id>', views.api_read, name="api.read.episode"),
    path('api/v1/update/<int:id>', views.api_update, name="api.update.episode"),
    path('api/v1/delete/<int:id>', views.api_delete, name="api.delete.episode"),
]