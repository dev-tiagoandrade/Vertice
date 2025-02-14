from django.db import models
from core.models import BaseModel, CHOICE
from clientes.models import Cliente
from funcionarios.models import Operador
from produtos.models import Produto


class Venda(BaseModel):
    dt_venda = models.DateTimeField("Data da Venda", auto_now_add=True)
    total_venda = models.DecimalField("Total da Venda", max_digits=10, decimal_places=2)
    mtd_pagamento = models.PositiveSmallIntegerField("Método de Pagamento", choices=CHOICE.METODO_PAGAMENTO)
    status = models.CharField("Status da Venda", max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cliente")
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE, verbose_name="Operador")
    
    def __str__(self):
        return f"Venda {self.id} - {self.dt_venda}"
    
    class Meta:
        db_table = "venda"
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"
        ordering = ["-dt_venda"]


class ItemVenda(BaseModel):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name="itens", verbose_name="Venda")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="itens_venda", verbose_name="Produto")
    quantidade = models.DecimalField("Quantidade", max_digits=10, decimal_places=2)
    preco_unitario = models.DecimalField("Preço Unitário", max_digits=10, decimal_places=2)
    desconto = models.DecimalField("Desconto", max_digits=10, decimal_places=2, default=0)
    cdg_especifico = models.CharField("Código Específico", max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f"ItemVenda {self.id} da Venda {self.venda.id}"
    
    class Meta:
        db_table = "item_venda"
        verbose_name = "Item de Venda"
        verbose_name_plural = "Itens de Venda"


class Pagamento(BaseModel):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name="pagamentos", verbose_name="Venda")
    mtd_pagamento = models.PositiveSmallIntegerField("Método de Pagamento", choices=CHOICE.METODO_PAGAMENTO)
    val_pagamento = models.DecimalField("Valor do Pagamento", max_digits=10, decimal_places=2)
    status = models.PositiveSmallIntegerField("Status do Pagamento", choices=CHOICE.STATUS_PAGAMENTO)
    
    def __str__(self):
        return f"Pagamento {self.id} da Venda {self.venda.id}"
    
    class Meta:
        db_table = "pagamento"
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"

