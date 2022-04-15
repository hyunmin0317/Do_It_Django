from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from blog.models import Post, Category, Tag


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'hook', 'head_image', 'file_upload', 'category']



class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['category_less_post_count'] = Post.objects.filter(category=None).count()
        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['category_less_post_count'] = Post.objects.filter(category=None).count()
        return context

def cagegories_page(request, slug):
    if slug=='no-category':
        category='미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug = slug)
        post_list = Post.objects.filter(category = category)

    context = {
        'categories' : Category.objects.all(),
        'category_less_post_count' : Post.objects.filter(category=None).count(),
        'category' : category,
        'post_list' : post_list
    }
    return render(request, 'blog/post_list.html', context)

def show_tag_posts(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()
    context = {
        'categories': Category.objects.all(),
        'category_less_post_count': Post.objects.filter(category=None).count(),
        'tag': tag,
        'post_list': post_list
    }
    return render(request, 'blog/post_list.html', context)

# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#     return render(request, 'blog/index.html', {'post_list':posts})
#
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, 'blog/single_post_page.html', {'post':post})
