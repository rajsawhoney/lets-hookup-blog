from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from testapp import views

from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView


urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^$', views.ArticleListView.as_view(), name='home'),
    url(r'^testapp/', include('testapp.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include('testapp.api.urls')),
    url(r'^accounts/', include('accounts.urls')),
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
