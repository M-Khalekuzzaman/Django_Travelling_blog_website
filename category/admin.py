from django.contrib import admin
from category.models import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','slug','created_date')
    
    
admin.site.register(Category,CategoryAdmin)
