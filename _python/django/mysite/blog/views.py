from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post


# First handler - post_list
def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


# Second handler - post_detail
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year,
                             publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


# Add Class-handler ListView from Django
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3  # Show 3 post on page
    template_name = 'blog/post/list.html'  # Use template for create page of site
