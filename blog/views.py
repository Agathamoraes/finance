from django.shortcuts import render
from django.utils import timezone
from .models import Post


def index(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    #return render(request, 'blog/post_list.html', {'posts': posts})
    return render(request, 'blog/index.html')
    
def post_list (request):
    return render(request, 'blog/post_list.html')