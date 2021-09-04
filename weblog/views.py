from django.shortcuts import render, get_object_or_404
from .models import Topic


def post_list(request):
    post = Topic.published.all()
    return render(request, 'templates/weblog/post_list.html', {'post': post})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Topic, publish__year=year, publish__month=month, publish__day=day,
                             slug=slug, status='published')
    return render(request, 'templates/weblog/post_detail.html', {'post': post})
