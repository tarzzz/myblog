from rest_framework.viewsets import ModelViewSet

from myblog.blog.models import BlogPost
from myblog.blog.serializers import BlogPostSerializer


class BlogPostsViewSet(ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
