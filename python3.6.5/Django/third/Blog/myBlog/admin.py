from django.contrib import admin

# Register your models here.
from myBlog.models import BlogsPost
class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title','timestamp']

admin.site.register(BlogsPost,BlogsPostAdmin)
