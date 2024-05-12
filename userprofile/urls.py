from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.profile, name = 'profile'),
    path('my_blogs/',views.my_blogs, name = 'my_blogs'),
    path('delete/<int:blog_id>/',views.delete_blog, name = 'delete_blog'),
    path('edit_blog/<int:blog_id>/',views.edit_blog, name = 'edit_blog'),
    
]
