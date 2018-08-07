from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from blog import urls as blog_urls
from blog.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home_page"),
    path('blog/', include(blog_urls)),   
]
