from django.contrib.syndication.views import Feed
from django.utils import timezone
from .models import Post


class LatestPostsFeed(Feed):
    title = "Forum DevOps Blog"
    link = "/"
    description = "Noticias e guias recentes para profissionais de DevOps."

    def items(self):
        return Post.objects.filter(is_published=True, published_at__lte=timezone.now())[:20]

    def item_title(self, item):
        return item.safe_translation_getter("title", any_language=True)

    def item_description(self, item):
        return item.safe_translation_getter("summary", any_language=True) or ""

    def item_link(self, item):
        return item.get_absolute_url()
