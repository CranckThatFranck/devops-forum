from django.core.management.base import BaseCommand
from django.utils import timezone
from blog.models import Category, Post


class Command(BaseCommand):
    help = "Seed starter categories and posts with translations."

    def handle(self, *args, **options):
        categories = [
            {
                "key": "automation",
                "pt": {"name": "Automacao", "slug": "automacao"},
                "en": {"name": "Automation", "slug": "automation"},
                "es": {"name": "Automatizacion", "slug": "automatizacion"},
            },
            {
                "key": "platform",
                "pt": {"name": "Plataforma", "slug": "plataforma"},
                "en": {"name": "Platform", "slug": "platform"},
                "es": {"name": "Plataforma", "slug": "plataforma"},
            },
        ]

        category_map = {}
        for item in categories:
            category = Category.objects.create()
            for code in ("pt-br", "en", "es"):
                category.set_current_language(code)
                data = item["pt" if code == "pt-br" else code]
                category.name = data["name"]
                category.slug = data["slug"]
                category.save()
            category_map[item["key"]] = category

        posts = [
            {
                "category": "automation",
                "pt": {
                    "title": "Primeiros passos com automacao de infraestrutura",
                    "slug": "primeiros-passos-automacao-infra",
                    "summary": "Como organizar automacao de infra sem caos.",
                    "body": "Este guia mostra uma rota simples para iniciar automacao de infraestrutura com foco em seguranca e repetibilidade.",
                },
                "en": {
                    "title": "Getting started with infrastructure automation",
                    "slug": "getting-started-infra-automation",
                    "summary": "How to start infra automation without chaos.",
                    "body": "This guide walks through a practical path to automate infrastructure with safety and repeatability in mind.",
                },
                "es": {
                    "title": "Primeros pasos con automatizacion de infraestructura",
                    "slug": "primeros-pasos-automatizacion-infra",
                    "summary": "Como empezar automatizacion sin caos.",
                    "body": "Esta guia muestra un camino simple para automatizar infraestructura con foco en seguridad y repetibilidad.",
                },
            },
            {
                "category": "platform",
                "pt": {
                    "title": "Checklist para ambientes de producao confiaveis",
                    "slug": "checklist-producao-confiavel",
                    "summary": "Itens basicos para elevar confiabilidade.",
                    "body": "Vamos cobrir observabilidade, backups, rollout seguro e praticas essenciais para ambientes de producao.",
                },
                "en": {
                    "title": "Checklist for reliable production environments",
                    "slug": "checklist-reliable-production",
                    "summary": "Core items to improve reliability.",
                    "body": "We cover observability, backups, safe rollout, and the essentials for reliable production.",
                },
                "es": {
                    "title": "Checklist para produccion confiable",
                    "slug": "checklist-produccion-confiable",
                    "summary": "Elementos clave para confiabilidad.",
                    "body": "Cubrimos observabilidad, backups, despliegues seguros y lo esencial para produccion confiable.",
                },
            },
        ]

        for item in posts:
            post = Post.objects.create(
                category=category_map[item["category"]],
                is_published=True,
                published_at=timezone.now(),
            )
            for code in ("pt-br", "en", "es"):
                post.set_current_language(code)
                data = item["pt" if code == "pt-br" else code]
                post.title = data["title"]
                post.slug = data["slug"]
                post.summary = data["summary"]
                post.body = data["body"]
                post.save()

        self.stdout.write(self.style.SUCCESS("Seed content created."))
