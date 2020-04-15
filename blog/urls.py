from django.urls import path
from .views import (
    PostListView,
    post_deatil_view,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    RoomCategoryView,
    RoomCategoryCreateView
)
from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    path("post/<int:pk>",views.post_deatil_view, name="post-detail"),
    path("post/new", PostCreateView.as_view(), name="post-create"),
    path("post/new/category", RoomCategoryCreateView.as_view(), name="room-category-create"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"),
    path("about/", views.about, name="blog-about"),
]

# TemplateDoesNotExist at /

# blog/post_list.html
# <app>/<model>_<viewtype>.html
