from django.contrib import admin
from .models import Blog,Comment,Tag,Reply

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','category','modified_date')
    
admin.site.register(Blog,BlogAdmin)

admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Reply)
