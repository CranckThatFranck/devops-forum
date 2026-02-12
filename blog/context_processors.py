from django.conf import settings


def site_settings(request):
    return {
        "site_brand": getattr(settings, "SITE_BRAND", "Forum DevOps"),
        "forum_url": getattr(settings, "FORUM_URL", "https://forumdevops.com"),
    }
