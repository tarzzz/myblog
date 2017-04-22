from rest_framework.serializers import ModelSerializer

from myblog.blog.models import BlogPost


class BlogPostSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
