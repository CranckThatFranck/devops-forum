from django.db import models
from django.urls import reverse
from django.utils import timezone
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100),
        slug=models.SlugField(max_length=120),
    )

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True) or "Category"


class Post(TranslatableModel):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="posts")
    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        slug=models.SlugField(max_length=220),
        summary=models.TextField(blank=True),
        body=models.TextField(),
    )
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "Post"

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.safe_translation_getter("slug", any_language=True)})
