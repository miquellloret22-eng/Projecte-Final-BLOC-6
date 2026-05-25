from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="index"),
    path("posts/", views.posts, name="posts"),
    path("posts/<slug:slug>", views.post_details, name="post-details"),
    path("authors/", views.authors, name="authors"),
    path("authors/<int:id>", views.author_details, name="author-details")
]