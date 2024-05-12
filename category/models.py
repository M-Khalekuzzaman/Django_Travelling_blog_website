from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length = 50,unique = True)
    slug = models.SlugField(max_length = 100,unique = True)
    description = models.TextField(max_length = 255,blank = True)
    cat_image = models.ImageField(upload_to = 'photos/categories', blank = True)
    created_date = models.DateTimeField(auto_now_add = True)
    
    def get_url(self):
        return reverse('blogs_by_category',args = [self.slug])
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    
