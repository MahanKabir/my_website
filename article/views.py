from django.shortcuts import render, redirect
from category.models import Category
from .models import Article
from .forms import ArticleForm
# Create your views here.


def create(request, id):
    category = Category.objects.get(id=id)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.category_id = id
            f.save()
            return redirect('read.cat')

    return render(request, 'article/create.html', {'category': category})

def read(request, id):
    articles = Article.objects.filter(category_id=id)
    category = Category.objects.get(id=id)

    return render(request, 'article/show.html', {'articles': articles, 'category': category})

def update(request):
    pass

def delete(request):
    pass
