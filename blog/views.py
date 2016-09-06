from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def v_post_list(request):
  # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  posts = Post.objects.filter()
  return render(request, 'blog/post_list.html', {'posts': posts} )

def v_post_detail(request, param_pk="1"):
  post = get_object_or_404(Post, pk=param_pk)
  return render(request, 'blog/post_detail.html', {'post': post})

