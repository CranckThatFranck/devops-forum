from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Post, Category


def home(request):
    posts = (
        Post.objects.filter(is_published=True, published_at__lte=timezone.now())
        .select_related("category")
        .prefetch_related("translations")
    )
    return render(request, "blog/home.html", {"posts": posts})


def category_detail(request, slug):
    category = get_object_or_404(Category, translations__slug=slug)
    posts = (
        category.posts.filter(is_published=True, published_at__lte=timezone.now())
        .select_related("category")
        .prefetch_related("translations")
    )
    return render(request, "blog/category_detail.html", {"category": category, "posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, translations__slug=slug, is_published=True)
    return render(request, "blog/post_detail.html", {"post": post})
