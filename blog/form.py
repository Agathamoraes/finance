from django import forms
from .models import Produto, Estoque, EstoqueItens, Parceiro

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class ParceiroForm(forms.ModelForm):
    class Meta:
        model = Parceiro
        fields = '__all__'

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ('nf','parceiro')

class EstoqueItensForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = '__all__'
