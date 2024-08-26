from django.shortcuts import render, get_object_or_404
from .models import Article, Jobs


def index(request):
    return render(request, "homepage/index.html")


def about(request):
    return render(request, "homepage/About_us.html")


def fleet(request):
    return render(request, "homepage/Fleet.html")


def advantage(request):
    return render(request, "homepage/Competitive_advantage")


def career(request):
    try:
        jobs = Jobs.objects.all()
    except Jobs.DoesNotExist:
        jobs = None
    return render(request, "homepage/Career.html", {"jobs": jobs})


def blog(request):
    latest_articles = Article.objects.order_by("-pub_date")[:3]
    return render(request, "homepage/blog.html", {"latest_articles": latest_articles})


def contact(request):
    return render(request, "homepage/Contact_us.html")


def articles(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    try:
        prev_article = Article.objects.get(pk=article_id-1)
    except Article.DoesNotExist:
        prev_article = None
    try:
        next_article = Article.objects.get(pk=article_id+1)
    except Article.DoesNotExist:
        next_article = None
    return render(
        request,
        "homepage/article.html",
        {"article": article, "prev_article": prev_article, "next_article": next_article})