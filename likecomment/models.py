from django.db import models
from django.contrib.auth.models import User
from testapp.models import Article
from tinymce.models import HTMLField
from django.urls import reverse
from accounts.models import UserModel


# Create your models here.


class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name=(
        "article"), on_delete=models.CASCADE, related_name='comments', null=True)
    user = models.ForeignKey(UserModel, verbose_name=(
        "UserName"), on_delete=models.CASCADE, null=True, blank=True,related_name='article_by')
    reply = models.ForeignKey("self", verbose_name=(
        "replies"), on_delete=models.CASCADE, null=True, blank=True, related_name="replies")
    comment_txt = models.TextField((''))
    commented_at = models.DateTimeField(("Commented On:"), auto_now_add=True)
    clapped = models.IntegerField(("Clapped Counts"), default=0)

    objects = models.Manager

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('commented_at',)

    def __str__(self):
        return str(self.comment_txt)[:100]

    def updateClap(self):
        self.clapped = self.clapped + 1
        self.save()

    def get_absolute_url(self):
        return reverse("testapp:edit_comment", kwargs={"pk": self.pk})
