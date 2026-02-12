# Implementation Guide

## Goal

Build and launch the DevOps community platform with:

- Forum as the primary product (Discourse)
- Blog as secondary (Django)
- Languages: PT-BR, EN, ES
- Domains: forumdevops.com (forum), blog.devops.com (blog)

## V1 Scope (Must Have)

- Forum: accounts, topics, replies, search, basic moderation, reporting
- Blog: public posts, categories, translations, SEO basics (sitemap + RSS)
- Auth: social login (Google, GitHub) + email
- Email: transactional (confirm, reset, notifications)
- Analytics: basic traffic tracking
- Branding: simple consistent visual kit

## Architecture (Simple)

- Discourse for the forum
- Django for the blog
- Separate subdomains with shared navigation
- Centralized docs and admin checklists

## Decisions Log

- Forum engine: Discourse (fast to launch, proven community features)
- Blog engine: Django (flexible publishing)
- Languages: PT-BR + EN + ES from day 1
- Moderation: basic rules + reporting, auto approval
- Auth: social + email
- Hosting: current Hostinger plan to be validated for Discourse (may need upgrade)

## Execution Checklist

### 1) Infrastructure

- Validate RAM and storage for Discourse (recommended 4GB RAM)
- Choose hosting path if Hostinger is not enough (upgrade or managed)
- Provision SSL certificates for both subdomains
- Set up backups and monitoring

### 2) DNS and Domains

- forumdevops.com -> Discourse host
- blog.devops.com -> Django host
- Configure SPF, DKIM, DMARC for email sender

### 3) Forum (Discourse)

- Install and configure Discourse
- Set site title, description, default language, and translations
- Create categories, tags, and posting guidelines
- Enable social login (Google, GitHub)
- Configure email provider for transactional emails
- Anti-spam and trust levels
- Enable backups and admin alerts

### Discourse Implementation (Hostinger)

Prerequisites checklist:
- Hostinger plan supports Docker and SSH access
- At least 2 vCPU and 4GB RAM recommended for Discourse
- Ports 80 and 443 open (HTTP/HTTPS)
- Domain forumdevops.com points to the server IP

Install steps (self-hosted):
1) Install Docker and Docker Compose
2) Clone Discourse Docker image repo
3) Configure app.yml (domain, SMTP, admin email)
4) Bootstrap and start Discourse container
5) Run initial web setup wizard
6) Configure languages and categories

Post-install:
- Configure backups and schedule
- Enable login via Google/GitHub
- Configure email deliverability (SPF/DKIM/DMARC)
- Enable basic anti-spam and rate limits

Inputs needed to proceed:
- SSH access to Hostinger server
- Confirmation Docker is allowed on the plan
- Forum admin email
- SMTP provider credentials

### 4) Blog (Django)

- Create Django project + app for blog
- Models: Post, Category, Translation
- Admin panel for publishing
- SEO basics: sitemap.xml, robots.txt, RSS
- Public pages: home, category, post
- Cross-link to forum

### Local Development (Blog)

1. Create and activate a virtual environment
2. Install requirements: `pip install -r requirements.txt`
3. Run migrations: `python manage.py makemigrations` then `python manage.py migrate`
4. Create admin user: `python manage.py createsuperuser`
5. Start server: `python manage.py runserver`

Environment variables (optional):

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG` (True/False)
- `DJANGO_ALLOWED_HOSTS` (comma-separated)
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
- `SITE_BRAND`
- `FORUM_URL`

### 5) Branding

- Define colors, typography, and logo placeholder
- Apply consistent header/footer across forum and blog

### 6) Analytics and Tracking

- Add analytics (Plausible or GA)
- Set up uptime monitoring

### 7) Pre-Launch

- Create starter content (5-10 posts)
- Create top-level forum threads
- Check email flows and redirects
- Load test basics

## V2 Ideas (Future)

- Monetization: banners and sponsorships
- Advanced search + content tagging
- User badges and gamification
- Integrations: job board, newsletter
- Editorial workflow for blog
- Community events and webinars

## Notes

- Keep decisions and changes logged here as the project evolves.
