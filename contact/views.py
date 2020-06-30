from accounts.forms import UserForm, UserProfileForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm

from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.conf import settings
from accounts.models import UserModel

from .models import Contact, Subscriber


# Create your views here.


class ContactListView(ListView):
    model = Contact
    template_name = "contacts-list.html"


class MessageDetailView(DetailView):
    model = Contact
    template_name = "message_detail.html"


class Thanks(TemplateView):
    template_name = "thanks.html"


def send_email(request):
    # subject = request.POST.get('subject', '')
    subject = "Reply from Lets-HookUp Contact Form"
    name = request.POST.get('name', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('to_email', '')
    to_email = settings.EMAIL_HOST_USER
    Subscriber.objects.create(subscriber=from_email)
    Contact.objects.create(name=name, email=from_email, message=message)
    if subject and message and from_email:
        try:
            send_mail(
                subject,
                message,
                to_email,
                [from_email, ]
            )
            mail_admins(subject, message)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')


def reply_message(request):
    if request.method == "POST":
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = settings.EMAIL_HOST_USER
        to_email = request.POST.get('email', '')
        if subject and message and to_email:
            try:
                send_mail(subject, message, from_email, [
                    to_email, ], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('contact_list/')


class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AuthenticationForm()
        context["user_profile_form"] = UserProfileForm()
        context["user_form"] = UserForm()
        if self.request.user.is_authenticated:
            context["user_object"] = get_object_or_404(
                UserModel, user=self.request.user)
        else:
            context["user_object"] = None

        return context
