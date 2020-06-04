from django.contrib import sitemaps
from django.urls import reverse
from testapp.models import Article, Category
from accounts.models import UserModel
from django.utils import timezone


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return [
            'testapp:home',
            'testapp:article-create',
            'testapp:category-create',
            'testapp:article-list',
            'testapp:article-category-list',
            'testapp:fav-article-list',
            'testapp:related-article-list',
            'testapp:authors-list',
            'about',
            'contact',

        ]

    def location(self, item):
        return reverse(item)


class ArticleSiteMap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return Article.objects.all()

    def lastmod(self, item):
        return item.last_updated


class ArticleCategorySiteMap(sitemaps.Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Category.objects.all()
