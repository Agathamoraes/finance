from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.views.generic import CreateView, UpdateView
from django.utils import timezone
from django.forms import inlineformset_factory
from .models import Produto,Estoque, EstoqueEntrada, EstoqueSaida, EstoqueItens
from .form import ProdutoForm, EstoqueForm, EstoqueItensForm

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

class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'blog/form_prod.html'
    form_class = ProdutoForm

def ent_estoque (request):
    template_name = 'blog/ent_estoque.html'
    objects = EstoqueEntrada.objects.all()
    context = {'object_list':objects}
    return render (request, template_name, context) 
    
def ent_estoque_detail (request, pk):
    template_name = 'blog/ent_estoque_detail.html'
    obj = EstoqueEntrada.objects.get(pk=pk)
    context = {'object':obj}
    return render (request, template_name, context) 

def baixa_estoque(form):
    #pega produto a partir da estancia do formulario
    produtos = form.estoques.all()
    for item in produtos:
        produto = Produto.objects.get(pk = item.produto.pk)
        produto.estoque = item.saldo
        produto.save()
    print('Estoque atualizado com sucesso')

def ent_estoque_form (request):
    template_name = 'blog/ent_estoque_form.html'
    estoque_form = Estoque()
    item_estoque_formset = inlineformset_factory(
        EstoqueEntrada,
        EstoqueItens,
        form = EstoqueItensForm,
        extra = 0,
        min_num = 1,
        validate_min = True,
        )
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance= estoque_form, prefix = 'main')
        formset = item_estoque_formset(request.POST, instance= estoque_form, prefix= 'estoque')
        if form.is_valid() and formset.is_valid():
            form = form.save()
            baixa_estoque(form)
            formset.save()
            url = 'blog:ent_estoque_detail'
            return HttpResponseRedirect(resolve_url(url, form.pk)) 
    else:
        form = EstoqueForm(instance= estoque_form, prefix = 'main')
        formset = item_estoque_formset(instance= estoque_form, prefix= 'estoque')

    context = {'form':form, 'formset':formset}
    return render (request, template_name, context) 

def produto_json(request, pk):
    #''' Retorna o produto, id e estoque. '''
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})

def sai_estoque_detail (request, pk):
    template_name = 'blog/sai_estoque_detail.html'
    obj = EstoqueSaida.objects.get(pk=pk)
    context = {'object':obj}
    return render (request, template_name, context) 


def sai_estoque (request):
    template_name = 'blog/sai_estoque.html'
    objects = EstoqueSaida.objects.all()
    context = {'object_list':objects}
    return render (request, template_name, context) 
  