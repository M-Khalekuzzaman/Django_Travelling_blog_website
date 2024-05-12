from django.urls import path
from . import views

urlpatterns = [
   path('blog/',views.blog, name = 'blog'),
   path('category/<slug:category_slug>/',views.blog, name = "blogs_by_category"),
   path('category/<slug:category_slug>/<slug:blog_slug>/',views.blog_detail, name = 'blog_detail'),
   path('search_blogs/',views.search_blogs, name = 'search_blogs'),
   path('search_related_blogs/',views.search_related_blogs, name = 'search_related_blogs'),
   path('add_reply/<int:blog_id>/<int:comment_id>/',views.add_reply, name = 'add_reply'),
   path('like_blog/<int:pk>/',views.like_blog, name = 'like_blog'),
   path('add_blog/',views.add_blog, name = 'add_blog'),

]
