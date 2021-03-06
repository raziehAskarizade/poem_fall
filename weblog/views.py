# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Topic


class PostListView(ListView):
    queryset = Topic.published.all()
    context_object_name = 'post'
    paginate_by = 3
    paginate_orphans = 1
    template_name = 'weblog/post/post_list.html'


# def post_list(request):
#     posts = Topic.published.all()
#     paginator = Paginator(posts, 3)
#     page_number = request.GET.get('page')
#     try:
#         # page_obj
#         post = paginator.page(page_number)
#     except PageNotAnInteger:
#         post = paginator.page(1)
#     except EmptyPage:
#         post = paginator.page(paginator.num_pages)
#
#     return render(request, 'weblog/post/post_list.html', {'page_number': page_number, 'post': post})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Topic, publish__year=year, publish__month=month, publish__day=day,
                             slug=slug, status='published')
    return render(request, 'weblog/post/post_detail.html', {'post': post})
