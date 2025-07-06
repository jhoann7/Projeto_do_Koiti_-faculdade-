from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'quantidade', 'preco']
        # Você pode personalizar labels, help_texts ou widgets aqui, se quiser
        labels = {
            'nome': 'Nome do Produto',
            'descricao': 'Descrição',
            'quantidade': 'Quantidade',
            'preco': 'Preço Unitário',
        }
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'preco': forms.NumberInput(attrs={'step': '0.01'}), # Permite valores decimais
        }