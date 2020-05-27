from __future__ import unicode_literals
import sys

from django.db import models
from django.urls import reverse

from django.utils.html import mark_safe

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

from gdstorage.storage import GoogleDriveStorage
from mytestwebsite import settings
# Define Google Drive Storage


class Photo(models.Model):
    gd_storage = GoogleDriveStorage()
    file = models.FileField(upload_to='ArticleAssets', storage=gd_storage)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
        ordering = ('-uploaded_at',)

    def save(self, *args, **kwargs):
        try:
            baseSize = 300
            print("Photo resing....")
            imageTemproary = Image.open(self.file)
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
            self.file = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" % self.file.name.split('.')[
                0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        except:
            print("Unable to open file...")
        super(Photo, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.file.name)

    def get_absolute_url(self):
        return reverse("testapp:gallery-detail", kwargs={"pk": self.pk})

    def image_tag(self):
        return mark_safe(f'<img src="{self.file.url}" width="150" height="150" alt="Missing or not an Image File" />')

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
