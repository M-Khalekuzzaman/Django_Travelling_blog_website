from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Account
from blog.models import Blog,Category
from blog.forms import AddBlogForm

@login_required(login_url='login')
def profile(request):
    blogs = request.user.user_blogs.all()
    blog_count = blogs.count()
    account = get_object_or_404(Account,pk = request.user.pk)
    context = {
        'blog_count' : blog_count,
        'account' : account
    }
    return render(request,'userprofile/profile.html',context)


@login_required(login_url='login')
def my_blogs(request):
    blogs = request.user.user_blogs.all()
    context = {
        'blogs' : blogs,
    }
    return render(request,'userprofile/my_blogs.html',context)

@login_required(login_url="login")
def delete_blog(request,blog_id):
    blog = Blog.objects.get(pk = blog_id).delete()
    return redirect('my_blogs')


def edit_blog(request,blog_id):
    blog = Blog.objects.get(pk = blog_id)
    form = AddBlogForm(instance = blog)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = AddBlogForm(request.POST, instance = blog)
        if form.is_valid():
            form.save(commit=True)
            return redirect('my_blogs')
    context = {
        'form': form,
        'categories' : categories
    }
    return render(request,"blog/add_blog.html",context)







