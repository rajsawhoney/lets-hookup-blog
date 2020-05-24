from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.shortcuts import render, reverse

# Create your models here.


def set_profile_Image_name(instance, filename):
    title = instance.user.username
    slug = slugify(title)
    return "user_profile_images/%s-%s" % (slug, filename)


class UserModel(models.Model):
    user = models.OneToOneField(User, verbose_name=(
        "user"), on_delete=models.CASCADE, null=True, related_name='users')
    about_me = models.TextField(
        ("About me:"), default="I am a good person!", blank=True)
    qualifications = models.TextField(
        ("Your Qualifications"), default="Bachelor's in Engineering", blank=True)

    profile_pic = models.ImageField(
        ("profile photo"), upload_to=set_profile_Image_name, blank=True)
    followed_by = models.ManyToManyField(
        "self", verbose_name=("Followed by"), blank=True, related_name='followers')

    favourites = models.ManyToManyField("testapp.Article", verbose_name=(
        "Favourite Articles"), related_name='fav_articles')

    def __str__(self):
        return self.user.username

    def how_much_articles(self):
        return self.articles.all().count()

    class Meta:
        verbose_name = ("UserModel")
        verbose_name_plural = ("UserModels")

    def get_update_url(self):
        return reverse("accounts:update-profile", kwargs={"pk": self.pk})

    def get_absolute_url(self):
        return reverse("accounts:myprofile", kwargs={"pk": self.pk})


class IPAddress(models.Model):
    ip = models.CharField(("Client IP"), max_length=50,)

    class Meta:
        verbose_name = ("IPAddress")
        verbose_name_plural = ("IPAddresses")

    def __str__(self):
        return self.ip
