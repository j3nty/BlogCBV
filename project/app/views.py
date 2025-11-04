from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from datetime import datetime
from .models import BlogPost, Category


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hour = datetime.now().hour
        if 0 <= hour < 6:
            greeting = "Доброй ночи"
        elif 6 <= hour < 12:
            greeting = "Доброе утро"
        elif 12 <= hour < 18:
            greeting = "Добрый день"
        else:
            greeting = "Добрый вечер"

        context["current_time"] = greeting
        return context


class PostListView(ListView):
    model = BlogPost
    context_object_name = "post_list"
    template_name = "post_list.html"
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(published=True).order_by("-created_at")


class CategoryPostListView(ListView):
    model = BlogPost
    template_name = "category_posts.html"
    context_object_name = "category_info"

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        category = get_object_or_404(Category, slug=slug)
        return BlogPost.objects.filter(category=category)