from django.db import models

# Create your models here.



class Category(models.Model):

    title = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='static/category/images/')
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)