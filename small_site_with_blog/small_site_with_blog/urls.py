from django.urls import path
from django.conf.urls import include

from django.contrib import admin

from blog import urls as blog_urls
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.home_page, name="home_page"),
    path('blog/', include(blog_urls)),   
]
