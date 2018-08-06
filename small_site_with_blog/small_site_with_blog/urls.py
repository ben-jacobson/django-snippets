#from django.contrib import admin
from django.urls import path

from blog import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home_page, name="home_page"),
    path('blog/', views.list_of_blog_posts, name="list_of_blog_posts"),
    path('blog/<int:blog_id>', views.blog_entry, name="list_of_blog_posts"),
]
