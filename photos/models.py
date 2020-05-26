from __future__ import unicode_literals
import sys

from django.db import models
from django.urls import reverse

from django.utils.html import mark_safe

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class Photo(models.Model):
    file = models.FileField(upload_to='ArticleAssets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
        ordering = ('-uploaded_at',)

    def save(self, *args, **kwargs):
        if self.file:
            print("Save method called!!")
            imageTemproary = Image.open(self.file)
            outputIoStream = BytesIO()
            w, h = imageTemproary.size
            imageTemproaryResized = imageTemproary.resize(
                (int(w/2), int(h/2)), Image.ANTIALIAS)
            imageTemproaryResized.save(
                outputIoStream, format='JPEG', quality=150)
            outputIoStream.seek(0)
            self.file = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" % self.file.name.split('.')[
                0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        super(Photo, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.file.name)

    def get_absolute_url(self):
        return reverse("testapp:gallery-detail", kwargs={"pk": self.pk})

    def image_tag(self):
        return mark_safe(f'<img src="{self.file.url}" width="150" height="150" alt="Missing or not an Image File" />')

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
