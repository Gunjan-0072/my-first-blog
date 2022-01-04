from django.shortcuts import render
from django.utils import timezone
from blog.models import PostBlog

# Create your views here.
def post_list(request):
    posts = PostBlog.objects.order_by('created_date')#filter(published_date__lte=timezone.now()) #.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
