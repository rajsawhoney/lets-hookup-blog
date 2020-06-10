from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import TemplateView, View, DetailView, ListView
from django.views.generic.edit import UpdateView, ModelFormMixin
from .models import UserModel
from django.contrib.auth.models import User
from .forms import UserForm, UserProfileForm, UserEditForm
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from testapp.models import Article
from django.template.loader import render_to_string

# Create your views here.


class UserModelListView(ListView):
    model = UserModel
    template_name = "authorslist.html"
    order_by = ()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["user_object"] = get_object_or_404(
                UserModel, user=self.request.user)
        else:
            context["user_object"] = None

        return context


class AboutView(TemplateView):
    template_name = "accounts/about.html"

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


class ContactView(TemplateView):
    template_name = "accounts/contact.html"

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


class UserModelDetailView(DetailView):
    model = UserModel
    template_name = "accounts/myprofile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AuthenticationForm()
        context["user_profile_form"] = UserProfileForm()
        context["user_form"] = UserForm()
        if self.request.user.is_authenticated:
            context["user_object"] = get_object_or_404(
                UserModel, user=self.request.user)
        else:
            context['user_object'] = None
        return context


class ChangePassword(auth_views.PasswordChangeView):
    template_name = 'accounts/password_change.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_object"] = get_object_or_404(
            UserModel, user=self.request.user)
        return context


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST or None)
        user_profile_form = UserProfileForm(
            request.POST, request.FILES, instance=UserModel())
        user_form = UserForm(request.POST, instance=User())
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            profile = user_profile_form.save(commit=False)
            profile.user = user
            profile.save()
            # user= authenticate(username=user,password=user_form.clean_password2)
            login(request, user)
            return redirect('testapp:article-list')

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('testapp:article-list')
    else:
        form = AuthenticationForm()
        user_profile_form = UserProfileForm()
        user_form = UserForm()

    if request.user.is_authenticated:
        user_object = get_object_or_404(UserModel, user=request.user)
    else:
        user_object = None

    context = {'user_form': user_form,
               'user_profile_form': user_profile_form, 'form': form, 'user_object': user_object, }

    return render(request, 'accounts/login.html', context)


class LogOutUser(auth_views.LogoutView):
    template_name = 'accounts/logged_out.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AuthenticationForm()
        context["user_profile_form"] = UserProfileForm()
        context["user_form"] = UserForm()

        return context


# def password_change(request):
#     changed = False
#     if request.method == 'POST':
#         form = PasswordChangeForm(user=request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             changed = True
#             return redirect('accounts:myprofile')
#         else:
#             print(form.errors)

#     else:
#         form = PasswordChangeForm(user=request.user)

#     return render(request, 'accounts/password_change.html', {'form': form})


class UserModelView(View):
    # decorators = [login_required, admin_hr_required] #decorators in case needed

    # @method_decorator(login_required)
    def get(self, request, pk=None):
        if pk and request.user.is_authenticated:  # user already exists so update case
            user = get_object_or_404(UserModel, id=pk)
            user_profile_form = UserProfileForm(instance=user)
            user_form = UserEditForm(instance=request.user)
            template = 'accounts/usermodel_update_form.html'
            context = {'user_form': user_form,
                       'user_profile_form': user_profile_form, }
        elif not pk and not request.user.is_authenticated:  # Sign Up Case i.e new user creation case
            user_profile_form = UserProfileForm()
            user_form = UserForm()
            template = 'accounts/signup.html'
            context = {'user_form': user_form,
                       'user_profile_form': user_profile_form, }
        return render(request, template, context)

    # @method_decorator(login_required)
    def post(self, request, pk=None):
        context = {}
        if pk:
            return self.put(request, pk)
        user_profile_form = UserProfileForm(
            request.POST, request.FILES, instance=UserModel())
        user_form = UserForm(request.POST, instance=User())
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            profile = user_profile_form.save(commit=False)
            profile.user = user
            profile.save()
            # user= authenticate(username=user,password=user_form.clean_password2)
            login(request, user)
            return redirect('testapp:article-list')
        context = {'user_form': user_form,
                   'user_profile_form': user_profile_form}
        return render(request, 'accounts/signup.html', context)

    # @method_decorator(decorators)
    def put(self, request, pk=None):
        context = {}
        user = get_object_or_404(UserModel, id=pk)
        user_profile_form = UserProfileForm(
            request.POST, request.FILES, instance=user)
        user_form = UserForm(request.POST, instance=request.user)

        if user_form.is_valid() and user_profile_form.is_valid():
            new_user = user_form.save()
            profile = user_profile_form.save(commit=False)
            profile.user = new_user
            profile.save()
            login(request, user)
            return redirect('testapp:article-list')
        context = {'user_form': user_form,
                   'user_profile_form': user_profile_form, }
        return render(request, 'accounts/signupform.html', context)

    # @method_decorator(decorators)
    def delete(self, request, pk=None):
        user = get_object_or_404(UserModel, id=pk)
        user.delete()
        return redirect('accounts:signup')


def follow_me(request):
    print("Follow me method called!!")
    crt_user = get_object_or_404(UserModel, user=request.user)
    if request.is_ajax():
        print(" Ajax method called!")
        userid = request.POST.get('id')
        user_to_be_followed = get_object_or_404(UserModel, id=userid)
        if user_to_be_followed in crt_user.followed_by.all():
            crt_user.followed_by.remove(user_to_be_followed)
            return JsonResponse({'success': 'unfollowed'})
        else:
            crt_user.followed_by.add(user_to_be_followed)
            return JsonResponse({'success': 'followed'})

    return HttpResponse("Warning! Please have an Ajax Request!!!")

# This is not the right place for this view


def add_remove_frm2fav(request, slug):
    article = get_object_or_404(Article, slug=slug)
    author = get_object_or_404(UserModel, user=request.user)
    if article in author.favourites.all():
        author.favourites.remove(article)
        print("Removed from ur FavList")
    else:
        author.favourites.add(article)
        print("Added to ur FavList")
    context = {'post': article, 'user_object': author}

    if request.is_ajax():
        print('Caught an Ajax request...')
        html = render_to_string(
            'includes/toggle-fav-article-snippet.html', context=context, request=request)
        return JsonResponse({'fav_data': html})

    return render(request, 'article-detail.html', context=context)


def toggle_mode(request):
    if request.is_ajax():
        mode = request.session.get('dark_mode')
        if mode:
            request.session['dark_mode'] = False
            print("Light Mode Enabled!!!")
        else:
            request.session['dark_mode'] = True
            print("Dark Mode Enabled!!!")
        return JsonResponse({'status': request.session.get('dark_mode')})

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
