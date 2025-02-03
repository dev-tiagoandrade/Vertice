from django.db import models

from estoque.models import Produto
from gestao.models import Funcionario


class CHOICES:
    METODO_PAGAMENTO = (
        ('credito', 'Crédito'),
        ('debito', 'Débito'),
        ('dinheiro', 'Dinheiro'),
        ('pix', 'Pix'),
        ('cheque', 'Cheque'),
    )
    
    PARCELAS_PAGAMENTO = (
        (1, '1x'),
        (2, '2x'),
        (3, '3x'),
        (4, '4x'),
        (5, '5x'),
        (6, '6x')
    )
    
    class Meta:
        abstract = True


class Venda(models.Model):
    vendedor = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, verbose_name="Vendedor")
    dt_venda = models.DateTimeField('Data da Venda', auto_now_add=True)
    cpf_cliente = models.CharField('CPF do Cliente', max_length=14, blank=True, null=True)
    mtd_pagamento = models.CharField(choices=CHOICES.METODO_PAGAMENTO,max_length=10)
    parcelas = models.PositiveSmallIntegerField('Parcelas', choices=CHOICES.PARCELAS_PAGAMENTO, )
    total = models.FloatField('Valor Total', default=0)

    def __str__(self):
        return f"Venda #{self.id} - R$ {self.total:.2f}"

    class Meta:
        db_table = 'venda'
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'


class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens', verbose_name="Venda")
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, verbose_name="Produto")
    qtd_venda_produto = models.FloatField('Quantidade')
    preco_unitario = models.FloatField('Preço Unitário')
    subtotal = models.FloatField('Subtotal', editable=False)

    def save(self, *args, **kwargs):
        # Calcula o subtotal automaticamente: quantidade x preço unitário
        self.subtotal = self.qtd_venda_produto * self.preco_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.qtd_venda_produto} x {self.produto} - R$ {self.subtotal:.2f}"

    class Meta:
        db_table = 'item_venda'
        verbose_name = 'Item de Venda'
        verbose_name_plural = 'Itens de Venda'
