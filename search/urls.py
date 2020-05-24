from django.conf.urls import url
from .views import SearchResultView
app_name = 'search'
urlpatterns = [
    url(r'^$', SearchResultView.as_view(), name='result_list'),
]
