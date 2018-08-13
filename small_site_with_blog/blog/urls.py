from django.urls import path
from blog import views

#app_name = 'blog'
urlpatterns = [
    path('', views.list_of_blog_posts.as_view(), name="blog_entries"),
    path('<int:pk>/', views.blog_post.as_view(), name="blog_post"),
]
