from django.urls import path
from blog import views

urlpatterns = [
    path('', views.list_of_blog_posts.as_view(), name="blog_entries"),
    path('<int:blog_id>/', views.blog_post.as_view(), name="blog_post"),
]
