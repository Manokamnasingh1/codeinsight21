from django.contrib import admin
from .models import Post
# Ragister your models here

class PostAdmin(admin.ModelAdmin):
    class Media:
        css = {
             "all": ("css/main.css",)
        }
        js = ("js/Post.js",)

admin.site.register(Post,PostAdmin)

