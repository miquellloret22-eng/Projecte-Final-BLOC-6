from django.contrib import admin
from .models import Author, Tag, Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("date", "author")
    list_display = ("title", "author", "date")
    search_fields = ("title",)
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address")
    search_fields = ("first_name",)

class TagAdmin(admin.ModelAdmin):
    search_fields = ("caption",)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
