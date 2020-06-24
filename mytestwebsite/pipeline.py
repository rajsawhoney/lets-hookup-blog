from accounts.models import UserModel

from django.contrib.auth.models import User


def save_profile(backend, user, response, *args, **kwargs):
    print("Responses grabed...from..", str(backend), user)
    print(response)
    if user not in User.objects.all():
        if 'github' in str(backend):
            UserModel.objects.create(
                user=user,
                about_me=response['bio'],
                profile_pic=response['avatar_url']
            )
            print("GitHub User created!!")
        elif 'linkedin' in str(backend):
            UserModel.objects.create(
                user=user,
                profile_pic=response['profilePicture']['displayImage']
            )
            print("linkedin User created!!")

        elif 'twitter' in str(backend):
            UserModel.objects.create(
                user=user,
                about_me=response['description'],
                profile_pic=response['profile_banner_url']
            )
            print("twitter User created!!")

        elif 'facebook' in str(backend):
            UserModel.objects.create(
                user=user,
                profile_pic=response['picture']['data']['url']
            )
            print("facebook User created!!")
    else:
        print(user, "This user already exists!!!")
