<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="index"),
    path("posts/", views.posts, name="posts"),
    path("posts/<slug:slug>", views.post_details, name="post-details")
=======
from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="index"),
    path("posts/", views.posts, name="posts"),
    path("posts/<slug:slug>", views.post_details, name="post-details")
>>>>>>> d500bc5aa07b13dceb9cf0ff5334931561ee7d4d
]