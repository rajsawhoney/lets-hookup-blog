from gdstorage.storage import GoogleDriveStorage
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.shortcuts import render, reverse

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
# Create your models here.


def set_profile_Image_name(instance, filename):
    title = instance.user.username
    slug = slugify(title)
    return "user_profile_images/%s-%s" % (slug, filename)


class UserModel(models.Model):
    gdStorage = GoogleDriveStorage()
    user = models.OneToOneField(User, verbose_name=(
        "user"), on_delete=models.CASCADE, null=True, related_name='users')
    about_me = models.TextField(
        ("About me:"), default="I am a good person! I am this and that", blank=True)
    qualifications = models.TextField(
        ("Your Qualifications"), default="Bachelor's in Engineering", blank=True)

    profile_pic = models.FileField(
        ("profile photo"), upload_to="user_profile_pic", blank=True, storage=gdStorage)
    followed_by = models.ManyToManyField(
        "self", verbose_name=("Followed by"), blank=True, related_name='followers')

    favourites = models.ManyToManyField("testapp.Article", verbose_name=(
        "Favourite Articles"), related_name='fav_articles')

    dark_mode = models.BooleanField(("Dark or Light Mode"), default=False)

    def __str__(self):
        return self.user.username

    def how_much_articles(self):
        return self.articles.all().count()

    class Meta:
        verbose_name = ("UserModel")
        verbose_name_plural = ("UserModels")

    def save(self, *args, **kwargs):
        try:
            baseSize = 350
            print("Save method called!!")
            imageTemproary = Image.open(self.profile_pic)
            outputIoStream = BytesIO()
            w, h = imageTemproary.size
            if (baseSize / w < baseSize / h):
                factor = baseSize / h
            else:
                factor = baseSize / w
            size = (int(w * factor), int(h * factor))
            imageTemproaryResized = imageTemproary.resize(
                size, Image.ANTIALIAS)
            imageTemproaryResized.save(
                outputIoStream, format='JPEG', quality=50)
            outputIoStream.seek(0)
            self.profile_pic = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" % self.profile_pic.name.split('.')[
                0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        except:
            print("Unable to open file...")
        super(UserModel, self).save(*args, **kwargs)

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
