from django.shortcuts import render, get_object_or_404
from .models import Article, Jobs


def index(request):
    job = get_object_or_404(Jobs, pk=1)
    return render(request, "homepage/main.html", {"job": job})


def blog(request):
    article = get_object_or_404(Article, pk=1)
    return render(request, "homepage/blog.html", {"article": article})