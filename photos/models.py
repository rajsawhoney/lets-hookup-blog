from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

from django.utils.html import mark_safe


class Photo(models.Model):
    file = models.FileField(upload_to='ArticleAssets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
        ordering = ('-uploaded_at',)

    def __str__(self):
        return str(self.file.name)

    def get_absolute_url(self):
        return reverse("testapp:gallery-detail", kwargs={"pk": self.pk})

    def image_tag(self):
        return mark_safe(f'<img src="{self.file.url}" width="150" height="150" alt="Missing or not an Image File" />')

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
