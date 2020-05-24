from rest_framework import serializers

from testapp.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'slug', 'title', 'category', 'content',
                  'author', 'has_liked', 'views_count', 'thumbnail']
