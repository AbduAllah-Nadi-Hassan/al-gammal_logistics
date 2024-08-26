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