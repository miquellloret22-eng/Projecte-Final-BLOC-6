from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from datetime import date

all_posts = [
    {
        "slug": "pogramar-en-python",
        "image": "img1.jpg",
        "author": "Miquel",
        "date": date(2026, 5, 21),
        "title": "Programar en python",
        "except": "Python es un llengutge de programacio de codi obert i alt nivell, que ",
        "content": """
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Placeat tempore temporibus porro expedita ea aut deserunt
            sunt labore, adipisci veritatis dicta repellat nobis natus nam numquam! Commodi recusandae est deleniti?
            
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Placeat tempore temporibus porro expedita ea aut deserunt
            sunt labore, adipisci veritatis dicta repellat nobis natus nam numquam! Commodi recusandae est deleniti?
            
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Placeat tempore temporibus porro expedita ea aut deserunt
            sunt labore, adipisci veritatis dicta repellat nobis natus nam numquam! Commodi recusandae est deleniti?
        """
    },
    {
        "slug": "programing-is-fun",
        "image": "img1.jpg",
        "author": "Miquel",
        "date": date(2026, 3, 10),
        "title": "Programing is fun",
        "except": "Python es un llengutge de programacio de codi obert i alt nivell, que ",
        "content": """
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Placeat tempore temporibus porro expedita ea aut deserunt
            sunt labore, adipisci veritatis dicta repellat nobis natus nam numquam! Commodi recusandae est deleniti?
            
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Placeat tempore temporibus porro expedita ea aut deserunt
            sunt labore, adipisci veritatis dicta repellat nobis natus nam numquam! Commodi recusandae est deleniti?
            
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Placeat tempore temporibus porro expedita ea aut deserunt
            sunt labore, adipisci veritatis dicta repellat nobis natus nam numquam! Commodi recusandae est deleniti?
        """
    },
    {
        "slug": "no-se-que-mes-posar",
        "image": "img1.jpg",
        "author": "Miquel",
        "date": date(2023, 5, 21),
        "title": "No se que mes posar",
        "except": "Python es un llengutge de programacio de codi obert i alt nivell, que ",
        "content": """
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Placeat tempore temporibus porro expedita ea aut deserunt
            sunt labore, adipisci veritatis dicta repellat nobis natus nam numquam! Commodi recusandae est deleniti?
            
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Placeat tempore temporibus porro expedita ea aut deserunt
            sunt labore, adipisci veritatis dicta repellat nobis natus nam numquam! Commodi recusandae est deleniti?
            
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Placeat tempore temporibus porro expedita ea aut deserunt
            sunt labore, adipisci veritatis dicta repellat nobis natus nam numquam! Commodi recusandae est deleniti?
        """
    }
]

def starting_page(request):
    """
    Retorna index.html renderitzat
    """
    try:
        posts_ordenats = sorted(all_posts, key=lambda post: post["date"], reverse=True)
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
        return render(request, "blog/posts.html", {
            "all_posts": all_posts
        })
    
    except:
        raise Http404()

def post_details(request, slug):
    """
    Retorna detalls.html renderitzat
    """
    try:

        post = next(p for p in all_posts if p["slug"] == slug)
        
        return render(request, "blog/detalls.html", {
            "post": post
        })
    
    except:
        raise Http404()