from django.shortcuts import render
from .models import Comment
from testapp.models import Article
from django.shortcuts import HttpResponse, get_object_or_404
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from .forms import CommentForm
from django.views.generic import UpdateView

# Create your views here.


def likePost(request):
    post_id = request.POST.get('id')
    print(post_id)
    artObj = Article.objects.get(id=post_id)
    print("Here is the result")
    print(artObj)

    if request.user in artObj.has_liked.all():
        print("User already exists!")
        artObj.has_liked.remove(request.user)
    else:
        print("New liker for this Article...")
        artObj.has_liked.add(request.user)  # Creating Like Object

        # Sending an success response
    context = {
        'post': artObj,
    }

    if request.is_ajax():
        print("This is an ajax request...")
        html = render_to_string(
            'includes/like_section.html', context, request=request)
        return JsonResponse({'form': html})


def clapping(request):
    if request.is_ajax():
        comment = get_object_or_404(Comment, id=request.POST.get('pk'))
        comment.updateClap()
        html = render_to_string(
            'includes/clapping_snippet.html', {'comment': comment})
        return JsonResponse({'form': html})
    else:
        return HttpResponse("<h1> This is not an Ajax request</h1>")


# def update_comment_view(request, pk):
#     comment_ins = get_object_or_404(Comment, id=pk)

#     if request.method == "POST":
#         form = CommentForm(request.POST or None, instance=comment_ins)
#         if form.is_valid():
#             form.save()
#     else:
#         form = CommentForm(instance=comment_ins)
#     return render(request, 'includes/edit_comment_snippet.html', {'form': form, })


def put_edit_comment_form(request):
    if request.is_ajax():
        comment_id = request.POST.get('comment_id')
        if comment_id:
            comment = get_object_or_404(Comment, id=comment_id)
            return JsonResponse({'comment_txt': comment.comment_txt, 'success': "ok", })
    else:
        return JsonResponse({'success': 'Failed', })


def edit_comment(request):
    if request.is_ajax():
        comment_id = request.POST.get('id')
        print('Edit comment section poked', comment_id)
        if comment_id:
            comment = get_object_or_404(Comment, id=comment_id)

            comment.comment_txt = request.POST.get('comment_txt')
            comment.save()

            current_article = get_object_or_404(Article, comments=comment)
            comments = Comment.objects.filter(
                article=current_article, reply=None)
            print("Comment updated successfully!")

            form = CommentForm(None)

            context = {
                'cmtform': form,
                'comments': comments,
                'post': current_article,
            }
            html = render_to_string(
                'includes/comment_section.html', context, request=request)

            return JsonResponse({'form': html})

        else:
            print("Failed to update this comment!!")
            return JsonResponse({'success': 'notok'})


# def comment(request):
#     if request.method =="POST":
#         form = CommentForm(request.POST or None)
#     if form.is_valid():
#         artObj = Article.objects.filter(id=request.POST.get('id'))
#         content = request.POST.get('comment_txt')


#     if article_id != None and content != None:
#         current_article = Article.objects.get(id=article_id)
#         c = Comment(article=current_article,
#                     user=request.user, comment_txt=content)
#         c.save()
#         comments = Comment.objects.filter(article=current_article, reply=None)
#         context = {
#         'comments': comments}
#     if request.is_ajax():
#         print("This is an ajax call...")
#         html = render_to_string(
#             'includes/comment_section.html', context, request=request)
#         return JsonResponse({'form': html})

#     else:
#         return HttpResponse('Do response related stuffs...')
