from django.utils.text import slugify
import random
import string


def generate_random_str(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a name character (char) field.
    """
    if new_slug is not None:
        slug = new_slug[:50]
    else:
        slug = slugify(instance.title[:50])

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=generate_random_str(size=5)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
