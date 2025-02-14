from django.forms import *
from .models import *
from fornecedores.models import Fornecedor


class ProdutoForm(ModelForm):
    # Campos extras para Fornecedor
    nm_fornecedor = CharField(
        widget=TextInput(attrs={
            'class': 'form-control form-control-solid',
            'placeholder': 'Nome do Fornecedor'
        }),
        label='Nome do Fornecedor',
        required=True
    )
    cnpj_fornecedor = CharField(
        widget=TextInput(attrs={
            'class': 'form-control form-control-solid',
            'placeholder': 'CNPJ do Fornecedor'
        }),
        label='CNPJ do Fornecedor',
        required=True
    )
    tel_fornecedor = CharField(
        widget=TextInput(attrs={
            'class': 'form-control form-control-solid',
            'placeholder': 'Telefone do Fornecedor'
        }),
        label='Telefone do Fornecedor',
        required=False
    )
    email_fornecedor = EmailField(
        widget=TextInput(attrs={
            'class': 'form-control form-control-solid',
            'placeholder': 'E-mail do Fornecedor'
        }),
        label='E-mail do Fornecedor',
        required=False
    )

    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'nm_produto': TextInput(attrs={
                'class': 'form-control form-control-solid',
                'placeholder': 'Nome do Produto'
            }),
            'cdg_produto': TextInput(attrs={
                'class': 'form-control form-control-solid',
                'placeholder': 'Código do Produto'
            }),
            'dsc_produto': Textarea(attrs={
                'class': 'form-control form-control-solid',
                'placeholder': 'Descrição detalhada do Produto',
                'rows': 3
            }),
            'preco_venda': NumberInput(attrs={
                'class': 'form-control form-control-solid',
                'placeholder': 'Preço de Venda'
            }),
            'preco_compra': NumberInput(attrs={
                'class': 'form-control form-control-solid',
                'placeholder': 'Preço de Compra'
            }),
            'margem_lucro': NumberInput(attrs={
                'class': 'form-control form-control-solid',
                'placeholder': 'Margem de Lucro (%)'
            }),
            'estoque_atual': NumberInput(attrs={
                'class': 'form-control form-control-solid',
                'placeholder': 'Estoque Atual'
            }),
            'estoque_minimo': NumberInput(attrs={
                'class': 'form-control form-control-solid',
                'placeholder': 'Estoque Mínimo'
            }),
            'und_medida': TextInput(attrs={
                'class': 'form-control form-control-solid',
                'placeholder': 'Unidade de Medida (ex.: UN, KG)'
            }),
            'venda_por_peso': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

    def save(self, commit=True):
        # Obtém os dados do fornecedor a partir do formulário
        cnpj = self.cleaned_data.get('cnpj_fornecedor')
        fornecedor, created = Fornecedor.objects.get_or_create(
            cnpj_fornecedor=cnpj,
            defaults={
                'nm_fornecedor': self.cleaned_data.get('nm_fornecedor'),
                'tel_forncedor': self.cleaned_data.get('tel_fornecedor'),
                'email_forncedor': self.cleaned_data.get('email_fornecedor')
            }
        )
        # Salva a instância do Produto, associando o fornecedor
        produto = super().save(commit=False)
        produto.fornecedor = fornecedor
        if commit:
            produto.save()
        return produto
