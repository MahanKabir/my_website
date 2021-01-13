
from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name="create.cat"),
    path('read', views.read, name="read.cat"),
    path('dashboard/read', views.dashboard_read, name="dashboard.cat"),
    path('update/<int:id>', views.update, name="update.cat"),
    path('delete/<int:id>', views.delete, name="delete.cat"),

    path('api/create', views.api_create, name="api.create.cat"),
    path('api/read', views.api_read, name="api.read.cat"),

]