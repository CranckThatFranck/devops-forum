from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone
from .models import Post


class StaticViewSitemap(Sitemap):
    priority = 0.6
    changefreq = "weekly"

    def items(self):
        return ["blog:home"]

    def location(self, item):
        return reverse(item)


class PostSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return Post.objects.filter(is_published=True, published_at__lte=timezone.now())

    def lastmod(self, obj):
        return obj.updated_at
