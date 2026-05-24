from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import date
from .models import Author, Post, Tag

def starting_page(request):
    """
    Retorna index.html renderitzat
    """
    try:
        ll_posts = Post.objects.all()
        posts_ordenats = sorted(ll_posts, key=lambda post: post.date, reverse=True)
        ultims_posts = posts_ordenats[0:3]
        return render(request, "blog/index.html", {
            "ultims_posts": ultims_posts
        })
    
    except:
        raise Http404()

def posts(request):
    """
    Retorna posts.html renderitzat
    """
    try:
        ll_posts = Post.objects.all()
        posts_ordenats = sorted(ll_posts, key=lambda post: post.date, reverse=True)
        return render(request, "blog/posts.html", {
            "all_posts": posts_ordenats
        })
    
    except:
        raise Http404()

def post_details(request, slug):
    """
    Retorna detalls.html renderitzat
    """
    try:
        post = Post.objects.get(slug=slug)
        
        return render(request, "blog/detalls.html", {
            "post": post
        })
    
    except:
        raise Http404()