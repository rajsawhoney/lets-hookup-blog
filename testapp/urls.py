from django.conf.urls import url
from django.urls import path

from . import views
from accounts.views import UserModelListView, follow_me
from likecomment.views import edit_comment, clapping, likePost, put_edit_comment_form


app_name = 'testapp'

urlpatterns = [
    url(r'^$', views.ArticleListView.as_view(), name='home'),

    path('articles/', views.ArticleListView.as_view(), name='article-list'),

    path('articles/category/', views.CategoryListView.as_view(),
         name='article-category-list'),

    path("category/detail/<slug>/",
         views.CategoryDetailView.as_view(), name='article-category-detail'),

    path('favourite/articles/', views.FavArticleListView.as_view(),
         name='fav-article-list'),

    path('my/articles/', views.YourArticleListView.as_view(),
         name='my-article-list'),

    path('followed/articles/', views.RelatedArticleListView.as_view(),
         name='related-article-list'),

    path("article/detail/<slug>/",
         views.article_detail_view, name='article-detail'),

    path("article/update/<slug>/",
         views.update_article_view, name='article-update'),

    path("delete-article/",
         views.delete_article_view, name='article-delete'),

    url(r"^article/create/", views.ArticleCreateView.as_view(), name='article-create'),

    url(r"^category/create/", views.CategoryCreateView.as_view(),
        name='category-create'),

    url(r'^likepost/', likePost, name='likepost'),

    path('clapping/', clapping, name='clapping'),

    path('edit-comment/form/', put_edit_comment_form, name='edit_comment_form'),

    path('edit-comment/', edit_comment, name='edit_comment'),

    path('articles/follow/', follow_me, name='follow_me'),

    path('authors/list/', UserModelListView.as_view(), name='authors-list'),

    path("gallery_detail/<int:pk>/",
         views.GalleryDetailView.as_view(), name='gallery-detail'),

]
