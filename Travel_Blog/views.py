from django.shortcuts import render,redirect
from blog.models import Blog

def home(request):
    blogs = Blog.objects.all()
    blog_count = blogs.count()
    context = {
        'blogs' : blogs,
        'blog_count' : blog_count
    }
    return render(request,'home.html',context)