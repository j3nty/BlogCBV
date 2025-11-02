from django.contrib import admin
from django.urls import path
from app.views import HomePageView, PostListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
    path("posts/", PostListView.as_view(), name="post_list"),
]
