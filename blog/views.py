from django.shortcuts import render

from blog.models import Post


def index(request):
    posts = Post.objects.all().order_by('-pk')
    return render(request, 'blog/index.html', {'posts':posts})