

from django.utils import timezone
from faker import Faker
import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mytestwebsite.settings')
django.setup()
from testapp.models import Article
from accounts.models import UserModel


def create_post(N):
    fake = Faker()
    for _ in range(N):
        pk = random.choice([1, 2, 3, 4, 5])
        title = fake.name()
        Article.objects.create(title=title + " Post!!!",
                               author=UserModel.objects.get(id=pk),
                               content=fake.text(),
                               thumbnail='C:\\Users\\Acer\\Desktop\\djangoProjects\\mytestwebsite\\media\\user_article_thumbnail\\best-try-ever-article-Screenshot_77_Fjf0Wi6.png',
                               )


create_post(2)

print("DATA IS POPULATED SUCCESSFULLY.")
