from django.dispatch import receiver
from django.db.models.signals import pre_save
from utils.slugify_unique import unique_slug_generator
from contextlib import contextmanager
from ming.odm import session
from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField
from accounts.models import UserModel
import datetime
from django.utils import timezone


from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


# Create your models here.


def set_Image_name(instance, filename):
    title = instance.article
    slug = slugify(title)
    return f"user_article_images/{slug}-{filename}"


def set_category_thumbnail_name(instance, filename):
    title = instance.title
    slug = slugify(title)
    return f"article_category_thumbnail/{slug}-{filename}"


def set_thumbnail_name(instance, filename):
    title = instance.title
    slug = slugify(title)
    return f"user_article_thumbnail/{slug}-{filename}"


class Category(models.Model):
    title = models.CharField(("Blog Type"), max_length=100)
    description = models.TextField(("About Category"))
    cat_thumbnail = models.ImageField(("CategoryImage"),
                                      upload_to=set_category_thumbnail_name, null=True, blank=True)
    slug = models.SlugField(("Slug"), blank=True, null=True)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def save(self, *args, **kwargs):
        if self.cat_thumbnail:
            baseSize = 500
            imageTemproary = Image.open(self.cat_thumbnail)
            outputIoStream = BytesIO()
            w, h = imageTemproary.size
            if (baseSize / w < baseSize / h):
                factor = baseSize / h
            else:
                factor = baseSize / w
            size = (int(w / factor), int(h / factor))
            imageTemproaryResized = imageTemproary.resize(
                size, Image.ANTIALIAS)
            imageTemproaryResized.save(
                outputIoStream, format='JPEG', quality=95)
            outputIoStream.seek(0)
            self.cat_thumbnail = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" % self.cat_thumbnail.name.split('.')[
                0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("testapp:article-category-detail", kwargs={"slug": self.slug})


@receiver(pre_save, sender=Category)
def category_pre_save_receiver(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


class Article(models.Model):
    ONE_STAR = '1'
    TWO_STAR = '2'
    THREE_STAR = '3'
    FOUR_STAR = '4'
    FIVE_STAR = '5'
    RATINGS = [

        (ONE_STAR, 'one star'),
        (TWO_STAR, 'two star'),
        (THREE_STAR, 'three star'),
        (FOUR_STAR, 'four star'),
        (FIVE_STAR, 'five star'),

    ]

    title = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, verbose_name=(
        "Blog Category"), related_name='blog_type', blank=True, null=True)
    content = models.TextField(("Article description"))
    last_updated = models.DateTimeField(("Last Updated"))
    pub_date = models.DateTimeField(auto_now_add=True)
    has_liked = models.ManyToManyField(User, verbose_name=(
        "Likers"), blank=True, related_name='likes')
    ratings = models.CharField(
        'ratings', max_length=2, choices=RATINGS, default=ONE_STAR)
    author = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, blank=True, null=True, related_name='articles')
    thumbnail = models.ImageField(
        ("Thumbnail"), upload_to=set_thumbnail_name, null=True, blank=True)
    assets = models.ManyToManyField("photos.Photo")
    slug = models.SlugField(null=True, blank=True)
    views_count = models.IntegerField(("Viewed"), default=0)
    client_ip = models.ManyToManyField("accounts.IPAddress", verbose_name=(
        "Client IP"), related_name='clients_ip', blank=True,)

    def save(self, *args, **kwargs):
        if not kwargs.pop('updatelasttime', False):
            self.last_updated = timezone.now()
            print("Last time field updated!!!")

        if self.thumbnail:
            baseSize = 500
            imageTemproary = Image.open(self.thumbnail)
            outputIoStream = BytesIO()
            w, h = imageTemproary.size
            if (baseSize / w < baseSize / h):
                factor = baseSize / h
            else:
                factor = baseSize / w
            size = (w / factor, h / factor)
            imageTemproaryResized = imageTemproary.resize(
                size, Image.ANTIALIAS)
            imageTemproaryResized.save(
                outputIoStream, format='JPEG', quality=95)
            outputIoStream.seek(0)
            self.thumbnail = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" % self.thumbnail.name.split('.')[
                0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        super(Article, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("testapp:article-detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("testapp:article-update", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("testapp:article-delete", kwargs={"slug": self.slug})

    def get_fav_article_url(self):
        return reverse("accounts:add-remove-fav", kwargs={"slug": self.slug})


@receiver(pre_save, sender=Article)
def article_pre_save_receiver(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

    # @contextmanager
    # def skip_last_updated(self, model_cls):
    #     skip_last_updated = getattr(
    #         session(model_cls)._get(), 'skip_last_updated', False)
    #     session(model_cls)._get().skip_last_updated = True
    #     try:
    #         yield
    #     finally:
    #         session(model_cls)._get().skip_last_updated = skip_last_updated

    class Meta:
        managed = True
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ("-last_updated",)


class Gallery(models.Model):
    article = models.ForeignKey(
        Article, verbose_name=("article_content"), on_delete=models.CASCADE, related_name='articles', null=True, blank=True)
    gallery_content = models.FileField(
        ("Gallery"), upload_to='uploaded_using_plugin/')

    class Meta:
        verbose_name = ("Gallery")
        verbose_name_plural = ("Galleries")

    def __str__(self):
        return str(self.gallery_content.name)

    def get_absolute_url(self):
        return reverse("testapp:gallery-detail", kwargs={"pk": self.pk})
