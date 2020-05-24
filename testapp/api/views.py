from django.http import Http404, JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView
from testapp.models import Article
from .serializers import ArticleSerializer
from django.shortcuts import get_object_or_404
from accounts.models import UserModel

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny


class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny, ]
