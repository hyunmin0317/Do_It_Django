from django.shortcuts import render

from blog.models import Post


def index(request):
    posts = Post.objects.all().order_by('-pk')
    return render(request, 'blog/post_list.html', {'post_list':posts})

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})