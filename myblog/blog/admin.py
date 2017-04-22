from django.contrib import admin

from myblog.blog.models import BlogPost, UserProfile


admin.site.register(BlogPost)
admin.site.register(UserProfile)
