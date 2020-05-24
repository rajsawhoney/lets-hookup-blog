from django.db import models

# Create your models here.


class ModelFirst(models.Model):
    name = models.CharField(("Name"), max_length=50)
    address = models.CharField(("Address"), max_length=50)

    class Meta:
        verbose_name = ("ModelFirst")
        verbose_name_plural = ("ModelFirsts")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("ModelFirst_detail", kwargs={"pk": self.pk})


class ModelSecond(models.Model):
    person = models.ForeignKey(ModelFirst, verbose_name=(
        "Person"), on_delete=models.CASCADE, blank=True)
    profession = models.CharField(("Profession"), max_length=50)

    class Meta:
        verbose_name = ("ModelSecond")
        verbose_name_plural = ("ModelSeconds")

    def __str__(self):
        return str(self.person.name)
