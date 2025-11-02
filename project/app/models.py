from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)


class AuthorProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name="user",
        on_delete=models.CASCADE,
    )


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(
        AuthorProfile,
        related_name="author",
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Category,
        related_name="category",
        on_delete=models.CASCADE,
    )
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse("blog", kwargs={"pk": self.pk, "slug": self.slug})
