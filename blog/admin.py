from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ("name",)


@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    list_display = ("title", "category", "is_published", "published_at")
    list_filter = ("is_published", "category")
    search_fields = ("translations__title", "translations__summary")
