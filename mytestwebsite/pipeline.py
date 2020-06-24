from accounts.models import UserModel


def save_profile(backend, user, response, *args, **kwargs):
    print("Responses grabed...from..", backend, user)
    print(response)
