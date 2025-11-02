from django.contrib import admin
from .models import BlogPost, AuthorProfile, Category


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "content",
        "author",
        "category",
        "published",
    ]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ["user"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name",)}
