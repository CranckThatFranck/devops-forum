from django.urls import path
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from . import views
from .feeds import LatestPostsFeed
from .sitemaps import PostSitemap, StaticViewSitemap

app_name = "blog"

urlpatterns = [
    path("", views.home, name="home"),
    path("rss/", LatestPostsFeed(), name="rss_feed"),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": {"static": StaticViewSitemap, "posts": PostSitemap}},
        name="sitemap",
    ),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("category/<slug:slug>/", views.category_detail, name="category_detail"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
]
