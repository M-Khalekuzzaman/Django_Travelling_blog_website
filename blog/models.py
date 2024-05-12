from django.db import models
from accounts.models import Account
from category.models import Category
from django.urls import reverse
from django.utils.text import slugify

class Tag(models.Model):
    title = models.CharField(max_length = 50,unique = True)
    slug = models.SlugField(max_length = 200,unique = True)
    created_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
        
class Blog(models.Model):
    user = models.ForeignKey(
        Account,
        related_name = 'user_blogs',
        on_delete = models.CASCADE
    )
    tags = models.ManyToManyField(
        Tag,
        related_name = 'tag_blogs',
        blank = True
    )
    likes = models.ManyToManyField(
        Account,
        related_name = 'user_likes',
        blank = True
    )
    category = models.ForeignKey(
        Category,
        related_name = 'category_blogs',
        on_delete = models.CASCADE
    )
    title = models.CharField(max_length = 200,unique = True)
    slug = models.SlugField(max_length = 255,unique = True)
    description = models.TextField(max_length = 1000,blank = True)
    banner = models.ImageField(upload_to = 'photos/blog_banners',blank = True)
    is_available = models.BooleanField(default = True)
    created_date = models.DateTimeField(auto_now_add = True)
    modified_date = models.DateTimeField(auto_now = True)
   
    def __str__(self):
        return self.title
    
    def get_url(self):
        return reverse('blog_detail',args = [self.category.slug, self.slug])
    
    
class Comment(models.Model):
    user = models.ForeignKey(
        Account,
        related_name = 'user_comments', 
        on_delete = models.CASCADE
    )
    blog = models.ForeignKey(
        Blog,
        related_name = 'blog_comments',
        on_delete = models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.text
    
class Reply(models.Model):
    user = models.ForeignKey(
        Account,
        related_name = 'user_replies',
        on_delete = models.CASCADE
    )
    comment = models.ForeignKey(
        Blog,
        related_name = 'blog_replies',
        on_delete = models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.text

