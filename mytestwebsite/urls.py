from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from testapp import views

from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
from testapp.models import Article
from django.contrib import admin
from django.contrib.sites.models import Site

admin.site.unregister(Site)


class SiteAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'domain')
    readonly_fields = ('id',)
    list_display = ('id', 'name', 'domain')
    list_display_links = ('name',)
    search_fields = ('name', 'domain')


admin.site.register(Site, SiteAdmin)


sitemaps = {
    'static': StaticViewSitemap,
}


urlpatterns = [

    path('admin/', admin.site.urls),
    path('google6cebc7472dd08059.html', TemplateView.as_view(
        template_name='google6cebc7472dd08059.html')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    url(r'^$', views.ArticleListView.as_view(), name='home'),
    url(r'^testapp/', include('testapp.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include('testapp.api.urls')),
    url(r'^accounts/', include('accounts.urls'), name='acc'),
    url(r'^article_search/', include('search.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^photo-upload/', include('photos.urls')),
    url(r'^test/', include('checkapp.urls')),
    url(r'^$', TemplateView.as_view(
        template_name="index.html"), name='home'),
    url(r'^', include('django.contrib.auth.urls')),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
