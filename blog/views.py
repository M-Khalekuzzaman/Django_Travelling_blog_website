from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Blog,Comment,Reply,Tag
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CommentForm,ReplyForm,AddBlogForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from accounts.models import Account
from django.contrib import messages



def blog(request, category_slug=None):
    categories = None
    blogs = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        blogs = Blog.objects.filter(category=categories,is_available = True)
        paginator = Paginator(blogs,2)
        page = request.GET.get('page')
        paged_blogs = paginator.get_page(page)
        blog_count = blogs.count()
    else:
        blogs = Blog.objects.all().filter(is_available=True).order_by('id')
        blog_count = blogs.count()
        paginator = Paginator(blogs,4)
        page = request.GET.get('page')
        paged_blogs = paginator.get_page(page)

    context = {
        'blogs': paged_blogs,
        'blog_count': blog_count,
        'categories':categories,
    }
    return render(request, 'blog/blog.html', context)

def blog_detail(request,category_slug,blog_slug):
    form = CommentForm()
    try:
        single_blog = Blog.objects.get(category__slug = category_slug,slug = blog_slug)
        category = Category.objects.get(id = single_blog.category.id)
        related_blogs = category.category_blogs.all()
        tags = Tag.objects.order_by('created_date')[:5]
        liked_by = request.user in single_blog.likes.all()
        
        
    except Exception as e:
        raise e
    
    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                user = request.user,
                blog = single_blog,
                text = form.cleaned_data.get('text')
            )
            return redirect('blog_detail',category_slug =category_slug,blog_slug = blog_slug)
    context = {
        'single_blog' : single_blog,
        'related_blogs' : related_blogs,
        'tags' : tags,
        'form' : form,
        'liked_by' : liked_by
    }
    return render(request,'blog/blog_details.html',context)

@login_required(login_url = 'login')
def add_reply(request,blog_id,comment_id):
    blog = get_object_or_404(Blog,id = blog_id)
    if request.method == "POST":
        form =  ReplyForm(request.POST)
        if form.is_valid():
            comment = get_object_or_404(Comment,id = comment_id)
            Reply.objects.create(
                user = request.user,
                comment = comment,
                text = form.cleaned_data.get('text')
            )
    return redirect('blog_detail',slug = blog.slug)

def search_blogs(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            blogs = Blog.objects.order_by('created_date').filter(
               Q(description__icontains = keyword) |
               Q(title__icontains = keyword)
            )
            blog_count = blogs.count()
    context = {
        'blogs' : blogs,
        'blog_count' : blog_count
    }
    return render(request,'blog/blog.html',context)

def search_related_blogs(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            blogs = Blog.objects.order_by('created_date').filter(
               Q(description__icontains = keyword) |
               Q(title__icontains = keyword)
            )
            blog_count = blogs.count()
    context = {
        'blogs' : blogs,
        'blog_count' : blog_count
    }
    return render(request,'blog/blog.html',context)


@login_required(login_url='login')
def like_blog(request,pk):
    context = {}
    blog = get_object_or_404(Blog,pk = pk)
    
    if request.user in blog.likes.all():
        blog.likes.remove(request.user)
        context['liked'] = False
        context['like_count'] = blog.likes.all().count()
    else:
        blog.likes.add(request.user)
        context['liked'] = True
        context['like_count'] = blog.likes.all().count()
     
    return JsonResponse(context,safe=False)


@login_required(login_url='login')
def add_blog(request):
    form = AddBlogForm()
    categories = Category.objects.all()
    if request.method == "POST":
        form = AddBlogForm(request.POST, request.FILES)
        if form.is_valid():
            user = get_object_or_404(Account,pk = request.user.pk)
            category = get_object_or_404(Category,pk = request.POST['category'])
            blog = form.save(commit=False)
            blog.user = user
            blog.category = category
            blog.save()
            messages.success(request,"Blog added successfully !")
            return redirect('blog_detail',category_slug = category.slug, blog_slug = blog.slug)
        
        else:
            print(form.errors)
    
    context = {
        'form' : form,
        'categories' : categories
    }
    return render(request,'blog/add_blog.html',context)
    

