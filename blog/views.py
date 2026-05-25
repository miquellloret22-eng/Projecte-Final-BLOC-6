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

    post = Post.objects.get(slug=slug)
    return render(request, "blog/detalls.html", {
        "post": post
    })


def authors(request):
    """
    Retorna authors.html renderitzat
    """
    try:
        autors = Author.objects.all()
        return render(request, "blog/autors.html", {
            "autors": autors
        })
    
    except:
        raise Http404()

def author_details(request, id):
    """
    Retorna detals_autor.html renderitzat
    """
    try:
        autor = Author.objects.get(id=id)
        posts_autor = Post.objects.filter(author=autor)
        return render(request, "blog/detalls_autor.html", {
            "autor": autor,
            "posts_autor": posts_autor
        })

    except:
        raise Http404()

def tags(request):
    try:
        ll_tags = Tag.objects.all()
        return render(request, "blog/tags.html", {
            "ll_tags": ll_tags
        })
    
    except:
        Http404()

def tags_details(request, id):
    try:
        tag = Tag.objects.get(id=id)
        posts_tag = Post.objects.filter(tags=tag)
        return render(request, "blog/tag_details.html", {
            "tag": tag,
            "posts_tag": posts_tag
        })
    
    except:
        raise Http404()