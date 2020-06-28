from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render, reverse
from django.views.generic import View, ListView, TemplateView, CreateView, FormView, DetailView, UpdateView, DeleteView
from accounts.models import UserModel
from .models import Article
from .forms import ArticleForm, ArticleEditForm
from likecomment.models import Comment
from likecomment.forms import CommentForm
from accounts.models import IPAddress, UserModel
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages


from photos.models import Photo
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import UserForm, UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from plyer import notification

from django.core.paginator import Paginator
from testapp.forms import CategoryForm
from testapp.models import Category
from django.contrib.sitemaps import ping_google

# @method_decorator(csrf_exempt, name='get_context_data')


class ArticleListView(ListView):
    model = Article
    template_name = "article-list.html"
    paginate_by = 6

    # For notification Purpose
    # print("I am called>>>Remider!")
    # notification.notify(
    #     title="Website Status", message="Your Website is running swiftly! Thanks!!!", timeout=10)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request

        popular_articles = Article.objects.all().order_by('-views_count')[:5]
        context['popular_articles'] = popular_articles

        if request.method == "POST":
            print("This is a POST method!")
            form = CommentForm(request.POST or None)
        else:
            form = CommentForm()
        context['cmtform'] = form

        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
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

        context['user_form'] = user_form
        context['user_profile_form'] = user_profile_form
        context['form'] = form

        if self.request.user.is_authenticated:
            who_to_follow = []
            try:
                context['user_object'] = get_object_or_404(
                    UserModel, user=self.request.user)
                for user in UserModel.objects.all():
                    if user not in context['user_object'].followed_by.all():
                        who_to_follow.append(user)
            except:
                pass

        else:
            context['user_object'] = None
            who_to_follow = UserModel.objects.all()

        context['who_to_follow'] = who_to_follow
        return context


class CategoryListView(ListView):
    model = Category
    template_name = "article-category-list.html"
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not self.request.user.is_superuser:
            raise Http404(
                "Sorry sir! You are strictly prohibited from accessing this page. Only the admin can access this page")
        request = self.request
        popular_articles = Article.objects.all().order_by('-views_count')[:5]
        context['popular_articles'] = popular_articles

        if request.method == "POST":
            print("This is a POST method!")
            form = CommentForm(request.POST or None)
        else:
            form = CommentForm()
        context['cmtform'] = form

        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
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

        context['user_form'] = user_form
        context['user_profile_form'] = user_profile_form
        context['form'] = form

        if self.request.user.is_authenticated:
            context['user_object'] = get_object_or_404(
                UserModel, user=self.request.user)
            who_to_follow = []
            for user in UserModel.objects.all():
                if user not in context['user_object'].followed_by.all():
                    who_to_follow.append(user)

        else:
            context['user_object'] = None
            who_to_follow = UserModel.objects.all()

        context['who_to_follow'] = who_to_follow
        return context


class RelatedArticleListView(ListView):
    model = Article
    template_name = "article-list.html"
    paginate_by = 6
    context = None

    def get_queryset(self):
        ins_user = get_object_or_404(
            UserModel, user=self.request.user)
        writers = ins_user.followed_by.all()
        list_article = Article.objects.filter(
            author__in=writers).distinct().order_by('-last_updated')
        return list_article

    def get_context_data(self, **kwargs):
        self.context = super().get_context_data(**kwargs)
        if self.request.method == "POST":
            print("This is a POST method!")
            form = CommentForm(self.request.POST or None)
        else:
            form = CommentForm()

        if self.request.user.is_authenticated:
            self.context['user_object'] = get_object_or_404(
                UserModel, user=self.request.user)
            who_to_follow = []
            for user in UserModel.objects.all():
                if user not in self.context['user_object'].followed_by.all():
                    who_to_follow.append(user)

        else:
            self.context['user_object'] = None
            who_to_follow = UserModel.objects.all()

        self.context['who_to_follow'] = who_to_follow
        self.context['cmtform'] = form
        popular_articles = Article.objects.all().order_by('-views_count')[:5]
        self.context['popular_articles'] = popular_articles
        self.context['followed_list'] = True
        return self.context

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        # ***Here You can do Ajax related stuffs***

        # if request.is_ajax():
        #     print(" I am in for Ajax Action")
        #     html = render_to_string(
        #         'includes/article-list-view-handler.html', context=self.context, request=request)
        #     print("Your list ", html)
        #     return JsonResponse({'list_data': html})

        return response


class FavArticleListView(ListView):
    model = Article
    template_name = "article-list.html"
    paginate_by = 6

    def get_queryset(self):
        ins_user = get_object_or_404(
            UserModel, user=self.request.user)
        list_article = ins_user.favourites.all()
        print("Fav articles list ", list_article)
        return list_article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == "POST":
            print("This is a POST method!")
            form = CommentForm(self.request.POST or None)
        else:
            form = CommentForm()

        if self.request.user.is_authenticated:
            context['user_object'] = get_object_or_404(
                UserModel, user=self.request.user)
            who_to_follow = []
            for user in UserModel.objects.all():
                if user not in context['user_object'].followed_by.all():
                    who_to_follow.append(user)

        else:
            context['user_object'] = None
            who_to_follow = UserModel.objects.all()

        context['who_to_follow'] = who_to_follow
        context['cmtform'] = form
        popular_articles = Article.objects.all().order_by('-views_count')[:5]
        context['popular_articles'] = popular_articles
        context['fav_list'] = True

        return context


class YourArticleListView(ListView):
    model = Article
    template_name = "article-list.html"
    paginate_by = 4

    def get_queryset(self):
        ins_user = get_object_or_404(
            UserModel, user=self.request.user)
        list_article = ins_user.articles.all()
        print("Fav articles list ", list_article)
        return list_article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == "POST":
            print("This is a POST method!")
            form = CommentForm(self.request.POST or None)
        else:
            form = CommentForm()

        if self.request.user.is_authenticated:
            context['user_object'] = get_object_or_404(
                UserModel, user=self.request.user)
            who_to_follow = []
            for user in UserModel.objects.all():
                if user not in context['user_object'].followed_by.all():
                    who_to_follow.append(user)

        else:
            context['user_object'] = None
            who_to_follow = UserModel.objects.all()

        context['who_to_follow'] = who_to_follow
        context['cmtform'] = form
        popular_articles = Article.objects.all().order_by('-views_count')[:5]
        context['popular_articles'] = popular_articles
        context['my_list'] = True

        return context


class GalleryDetailView(DetailView):
    model = Photo
    template_name = "showpic.html"
    context_object_name = "gallery_obj"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_object'] = get_object_or_404(
                UserModel, user=self.request.user)
        else:
            context['user_object'] = None
        return context


# @method_decorator(csrf_exempt, name='get_context_data')
# class ArticleUpdateView(UpdateView):
#     model = Article
#     form_class = ArticleEditForm
#     template_name = "article_update.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         messages.success(self.request, "Article updated successfully!")
#         if self.request.is_ajax():
#             print("This is an ajax call I am calling update method...")
#             html = render_to_string(
#                 'includes/article_update_snippet.html', context, request=self.request)
#             return JsonResponse({'form': html})
#         return context


@csrf_exempt
def update_article_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == "POST":
        form = ArticleEditForm(request.POST or None,
                               request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Article updated successfully!")
        else:
            messages.warning(request, "Failed to Update!!!")

    else:
        form = ArticleEditForm(instance=article)

    if request.user.is_authenticated:
        current_user = get_object_or_404(UserModel, user=request.user)

    else:
        current_user = None

    context = {'form': form, 'user_object': current_user}

    if request.is_ajax():
        print("This is an Ajax Call from update form....")
        html = render_to_string(
            "includes/article_update_alert.html", context=context, request=request)
        return JsonResponse({'form': html})

    return render(request, "article_update.html", context)


def delete_article_view(request):
    if request.is_ajax():
        pk = request.POST.get('id')
        article = get_object_or_404(Article, id=pk)
        article.delete()
        messages.success(request, f"\"{article.title}\" successfully deleted!")
        try:
            ping_google(sitemap_url='/sitemap.xml')
        except Exception:
            pass
        return JsonResponse({'success': 'ok'})
    else:
        messages.warning(request, f"\"{article.title}\" failed to delete!!!")
        return JsonResponse({'success': 'not_ok'})


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class ArticleCreateView(LoginRequiredMixin, AjaxableResponseMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "create-article.html"
    success_url = '/testapp/my/articles/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_object'] = get_object_or_404(
                UserModel, user=self.request.user)
        else:
            context['user_object'] = None
        return context

    def form_valid(self, form):
        user = get_object_or_404(UserModel, user=self.request.user)
        form.instance.author = user
        form.save()
        try:
            ping_google(sitemap_url='/sitemap-articles.xml/')
        except Exception:
            pass
        messages.success(self.request, "New Article Successfully Published!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Failed to Publish New Article!!!")
        return super().form_invalid(form)


class CategoryCreateView(LoginRequiredMixin, AjaxableResponseMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "create-article-category.html"
    success_url = '/testapp/articles/category/'

    def get_context_data(self, **kwargs):
        if not self.request.user.is_superuser:
            raise Http404(
                "Sorry sir! You are strictly prohibited from accessing this page. Only the admin can access this page")
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_object'] = get_object_or_404(
                UserModel, user=self.request.user)
        else:
            context['user_object'] = None
        return context

    def form_valid(self, form):
        messages.success(
            self.request, "New Article Category Successfully Added!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(
            self.request, "Failed to Add a New Article Category!!!")
        return super().form_invalid(form)


class CategoryDetailView(DetailView):
    model = Category
    template_name = "category-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["user_object"] = get_object_or_404(
                UserModel, user=self.request.user)
            who_to_follow = []
            for user in UserModel.objects.all():
                if user not in context['user_object'].followed_by.all():
                    who_to_follow.append(user)

        else:
            context['user_object'] = None
            who_to_follow = UserModel.objects.all()

        context['who_to_follow'] = who_to_follow

        return context


# For Multi-File Upload Purpose

# class ArticleCreateView(FormView):
#     form_class = ArticleForm
#     template_name = 'create-article.html'
#     # Replace with your URL or reverse().
#     success_url = reverse_lazy('testapp:article-list')

#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('article_content')
#         if form.is_valid():
#             print(form.cleaned_data)
#             instance = form.save(commit=False)
#             instance.auther = request.user
#             instance.save()
#             print("Form is valid!")
#             for f in files:
#                 f = Gallery(gallery_content=f)
#                 print("saving to Gallery Model")
#                 print(f)
#                 f.save()

#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)


@csrf_exempt
def article_detail_view(request, slug):
    current_article = get_object_or_404(Article, slug=slug)
    related_posts = Article.objects.filter(
        category_in=current_article.category.all())

    # For num of Views handling
    client_ip_addr = request.META.get('REMOTE_ADDR')
    existing_ip = IPAddress.objects.filter(ip=client_ip_addr)
    if existing_ip.exists():
        print("This client ip already exists!!")
        ip_instance = IPAddress.objects.get(ip=client_ip_addr)
        if ip_instance in current_article.client_ip.all():
            print("This client has already viewed this post!")
        else:
            current_article.client_ip.add(ip_instance)
            current_article.views_count += 1
            current_article.save(updatelasttime=True)
            print("But visiting this post for the first time!")
    else:
        print("New IP caught!")
        ip_ins = IPAddress.objects.create(ip=client_ip_addr)
        current_article.views_count += 1
        current_article.client_ip.add(ip_ins)
        current_article.save(updatelasttime=True)

    popular_articles = Article.objects.all().order_by('-views_count')[:5]
    comments = Comment.objects.filter(
        article=current_article, reply=None)
    if request.user.is_authenticated:
        current_user = get_object_or_404(
            UserModel, user=request.user)
        who_to_follow = []
        for user in UserModel.objects.all():
            if user not in current_user.followed_by.all():
                who_to_follow.append(user)

    else:
        current_user = None
        who_to_follow = UserModel.objects.all()

    if request.method == "POST":
        print("This is a POST method!")
        cmtform = CommentForm(request.POST or None)
        if cmtform.is_valid():
            print("This is a valid form...")
            print(cmtform.cleaned_data)
            comment_txt = cmtform.cleaned_data['comment_txt']
            comment_id = request.POST.get('cmt_id')
            comment_qs = None
            if comment_id:
                print("This is going to be a reply...")
                comment_qs = Comment.objects.get(id=comment_id)
            q = Comment(user=current_user, comment_txt=comment_txt,
                        article=current_article, reply=comment_qs)
            q.save()
        else:
            print(cmtform.errors)

    else:
        cmtform = CommentForm()

    form = AuthenticationForm()
    user_profile_form = UserProfileForm()
    user_form = UserForm()
    context = {
        'cmtform': cmtform,
        'comments': comments,
        'post': current_article,
        'user_object': current_user,
        'popular_articles': popular_articles,
        'who_to_follow': who_to_follow,
        'form': form,
        'user_profile_form': user_profile_form,
        'user_form': user_form,
        'related_posts': related_posts,
    }

    if request.is_ajax():
        print("This is an ajax call... from comment section!!!")
        html = render_to_string(
            'includes/comment_section.html', context, request=request)
        return JsonResponse({'form': html})

    return render(request, 'article-detail.html', context=context)
