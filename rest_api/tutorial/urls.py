from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from tutorial.quickstart import views

# I suppose with Django REST, the routers work in a similar way to MVC controllers eg backbone? 

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)      # the regular expression here is called a prefix. The second argument is hte viewset class
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^', include(router.urls)),        # with include, you may append with namespace='instance_name' if you need 
    #url(r'^api-path', include('rest_framework.urls', namespace='rest_framework'))
    path('', include('snippets.urls')),
]

