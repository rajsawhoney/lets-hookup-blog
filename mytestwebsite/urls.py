"""mytestwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from testapp import views

from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.views.generic import TemplateView

dajaxice_autodiscover()

urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^$', views.ArticleListView.as_view(), name='home'),
    url(r'^testapp/', include('testapp.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include('testapp.api.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^article_search/', include('search.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^dajaxice/', include('dajaxice.urls')),
    url(r'^photo-upload/', include('photos.urls')),
    url(r'^test/', include('checkapp.urls')),
    url(r'^$', TemplateView.as_view(
        template_name="index.html"), name='home'),
    url(r'^', include('django.contrib.auth.urls')),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
