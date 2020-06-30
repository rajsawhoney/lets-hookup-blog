from django.db import models

# Create your models here.


class Subscriber(models.Model):
    subscriber = models.EmailField(
        ("subscriber_email"), max_length=254, unique=True)
    subscribed_on = models.DateTimeField(("subscribed_on"), auto_now=True)

    class Meta:
        verbose_name = ("Subscriber")
        verbose_name_plural = ("Subscribers")

    def __str__(self):
        return str(self.subscriber)


class Contact(models.Model):
    name = models.CharField(("Name"), max_length=50)
    email = models.EmailField(("Email"), max_length=254, unique=True)
    message = models.TextField(("Message"))
    sent_date = models.DateTimeField(("Sent On"), auto_now=True)
    read = models.BooleanField(("Read or Not Read"), default=False)

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("contact_detail", kwargs={"pk": self.pk})
