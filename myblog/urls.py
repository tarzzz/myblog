from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from blog.views import BlogPostsViewSet

router = DefaultRouter()
router.register(r'posts', BlogPostsViewSet, base_name='posts')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
