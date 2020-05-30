from django.shortcuts import render
from django.views.generic import CreateView
from django.utils import timezone
from .models import Produto
from .form import ProdutoForm

def index(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    #return render(request, 'blog/post_list.html', {'posts': posts})
    return render(request, 'blog/index.html')
    
def post_list (request):
    return render(request, 'blog/post_list.html')

def produto_list (request):
    template_name = 'blog/produto_list.html'
    objects = Produto.objects.all()
    context = {'object_list': objects}
    return render( request, template_name, context)

def detail_prod (request, pk):
    template_name = 'blog/detail_prod.html'
    obj = Produto.objects.get(pk=pk)
    context = {'object': obj}
    return render( request, template_name, context)

def produto_add(request):
    template_name= 'blog/form_prod.html'
    return render (request, template_name)

class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'blog/form_prod.html'
    form_class = ProdutoForm