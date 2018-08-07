from django.urls import path
from blog import views

urlpatterns = [
    path('', views.list_of_blog_posts, name="blog_entries"),
    path('<int:blog_id>/', views.blog_entry, name="blog_post"),
]
