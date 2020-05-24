from django.urls import path
from rest_framework.routers import DefaultRouter
from testapp.api.views import ArticleViewSet


router = DefaultRouter()
router.register(r'article', ArticleViewSet, basename='api')
urlpatterns = router.urls
