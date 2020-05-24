from django.shortcuts import get_object_or_404, render
from testapp.models import Article
from django.views.generic import TemplateView
from django.db.models import Q
from django.contrib import messages
from accounts.models import UserModel

# Create your views here.


class SearchResultView(TemplateView):
    template_name = "searchresult.html"

    def get_context_data(self, **kwargs):
        print("Getting context...")
        request = self.request
        querytxt = request.GET.get('q')
        search_by = self.request.GET.get('search_by', None)
        print("Search by ", search_by)
        context = super().get_context_data(**kwargs)
        if search_by == "Author":
            lookups = (Q(author__user__username__icontains=querytxt))
        elif search_by == "Category":
            lookups = (Q(category__title__icontains=querytxt))
        elif search_by == "Article Tags":
            lookups = (Q(title__icontains=querytxt) |
                       Q(content__icontains=querytxt)
                       )

        else:
            lookups = (Q(title__icontains=querytxt) |
                       Q(content__icontains=querytxt) |
                       # search by related model names
                       # reply is also filtered using comment content
                       Q(comments__comment_txt__icontains=querytxt) |
                       Q(author__user__username__icontains=querytxt) |
                       Q(category__description__icontains=querytxt) |
                       Q(category__title__icontains=querytxt)
                       )

        context['search_result'] = Article.objects.filter(lookups).distinct()
        if context['search_result'].exists():
            messages.success(
                request, f"\"{context['search_result'].all().count()} Articles Found related to your keyword '{querytxt}'")

        else:
            messages.warning(
                request, f"No Article Found for your keyword '{querytxt}'!!!")

        if self.request.user.is_authenticated:
            context['user_object'] = get_object_or_404(
                UserModel, user=self.request.user)
        else:
            context['user_object'] = None
        return context
