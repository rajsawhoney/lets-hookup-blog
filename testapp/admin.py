from django.contrib import admin

from .models import Article, Gallery, Category

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'views_count']

    class Meta:
        js = ('/static/js/tiny_mce/tiny_mce.js',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','slug']


admin.site.register(Gallery)
