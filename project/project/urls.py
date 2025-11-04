from django.contrib import admin
from django.urls import path
from app.views import HomePageView, PostListView, CategoryPostListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path(
        "category/<slug:slug>/",
        CategoryPostListView.as_view(),
        name="categories_by_slug",
    ),
]
