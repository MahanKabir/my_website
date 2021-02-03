
from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name="create.cat"),
    path('read', views.read, name="read.cat"),
    path('update/<int:id>', views.update, name="update.cat"),
    path('delete/<int:id>', views.delete, name="delete.cat"),

    path('api/create', views.api_create, name="api.create.cat"),
    path('api/read', views.api_read, name="api.read.cat"),
    path('api/update/<int:pk>', views.api_update, name="api.update.cat"),
    path('api/delete/<int:id>', views.api_delete, name="api.delete.cat"),

]