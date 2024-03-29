from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from quickstart import views


# Quickstart Router
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Tutorial
    url(r'^', include('snippets.urls')),

    # Quickstart urls
    url(r'quickstart^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
)
