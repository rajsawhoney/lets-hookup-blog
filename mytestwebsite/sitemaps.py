from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['testapp:home', 'testapp:article-list', 'testapp:article-category-list', 'testapp:fav-article-list', 'testapp:related-article-list', 'testapp:authors-list', ]

    def location(self, item):
        return reverse(item)
