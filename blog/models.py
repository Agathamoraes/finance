from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class TimeStampedModel (models.Model):
    created = models.DateTimeField(
         'Criado em ',
         auto_now_add=True,
         auto_now=False
    )
    modified = models.DateTimeField(
        'Modificado em',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        abstract = True

class Produto (models.Model):
    importado = models.BooleanField(default=False)
    ncm = models.CharField('NCM', max_length=8)
    produto = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField ('Preço', max_digits=7, decimal_places=2)
    estoque = models.IntegerField('Estoque Atual')
    estoque_minimo = models.PositiveIntegerField('Estoque Minímo', default=0)

    class meta:
        ordering= ('Produto')

    def __str__(self):
        return self.produto

    def get_absolute_url(self):
        return reverse_lazy('blog:detail_prod', kwargs={'pk': self.pk})
    
    def to_dict_json(self):
        return {
            'pk': self.pk,
            'produto': self.produto,
            'estoque': self.estoque,
        }

MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)

class Estoque (TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO, blank=True)

    class meta:
        ordenring = ('-created') 

    def __str__(self):
        if self.nf:
            return '{} - {} - {}'.format(self.pk, self.nf, self.created.strftime('%d-%m-%Y'))
        return '{} --- {}'.format(self.pk,self.created.strftime('%d-%m-%Y'))

    def nf_formated(self):
        if self.nf:
            return str (self.nf).zfill(3)
        return '---'

class EstoqueEntradaManeger(models.Manager):
    def get_queryset(self):
        return super(EstoqueEntradaManeger, self).get_queryset().filter(movimento = 'e')

class EstoqueEntrada(Estoque):
    objects = EstoqueEntradaManeger()
    class Meta:
        proxy = True
        verbose_name = 'estoque entrada'
        verbose_name_plural = 'estoque entrada' 
    def get_absolute_url(self):
        return reverse_lazy('blog:ent_estoque_detail', kwargs={'pk': self.pk})


class EstoqueSaidaManeger(models.Manager):
    def get_queryset(self):
        return super(EstoqueSaidaManeger, self).get_queryset().filter(movimento = 's')

class EstoqueSaida(Estoque):
    objects = EstoqueSaidaManeger()
    class Meta:
        proxy = True
        verbose_name = 'estoque saida'
        verbose_name_plural = 'estoque saida' 
    
    def get_absolute_url(self):
        return reverse_lazy('blog:sai_estoque_detail', kwargs={'pk': self.pk})


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, related_name='estoques')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField()

    class Meta:
        ordering=('pk',)

    def __str__(self):
        return '{} - {} - {}'.format (self.pk, self.estoque.pk, self.produto)

    