from django.shortcuts import render
from blog1.models import Post,Category

def home(self):
    posts=Post.objects.all()[:5]
    cats=Category.objects.all()
    data={
        'posts':posts,
        'category':cats
    }
    return render(self,"index.html",data)
# Create your views here.

def post(request, url):
    post=Post.objects.get(url=url)
    cats=Category.objects.all()
    return render(request,"post.html",{'post':post,'category':cats})

def category(request,url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    return render(request,"category.html",{'cat':cat,'posts':posts})
