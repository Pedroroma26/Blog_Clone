from django.contrib import admin
from .models import Post, Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):

    fields = ['author', 'title', 'text', 'created_date', 'published_date']

    search_fields = ['author']

    list_filter = ['author', 'title' , 'published_date']

    list_display = ['published_date', 'author', 'title']

    list_editable = ['author', 'title']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
