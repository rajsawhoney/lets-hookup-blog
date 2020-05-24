from django.conf.urls import url
from .views import BiModelFormView


urlpatterns = [
    url(r'^$', BiModelFormView, name='checkform'),
]
