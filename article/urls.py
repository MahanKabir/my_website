from django.urls import path
from . import views
urlpatterns = [
    path('create/<int:id>', views.create, name="create.article"),
    path('read/<int:id>', views.read, name="read.article"),
    path('update/<int:id>', views.update, name="update.article"),
    path('delete/<int:id>', views.delete, name="delete.article"),
]