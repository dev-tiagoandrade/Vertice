from django.db import models
from core.models import BaseModel, CHOICE
from fornecedores.models import Fornecedor
from produtos.models import Produto


class Compra(BaseModel):
    dt_compra = models.DateTimeField("Data da Compra", auto_now_add=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name="compras", verbose_name="Fornecedor")
    total_compra = models.DecimalField("Total da Compra", max_digits=10, decimal_places=2)
    status = models.PositiveSmallIntegerField("Status da Compra", choices=CHOICE.STATUS_COMPRA)
    
    def __str__(self):
        return f"Compra {self.id} - {self.fornecedor.nm_fornecedor}"
    
    class Meta:
        db_table = "compra"
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        ordering = ["-dt_compra"]


class ItemCompra(BaseModel):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens", verbose_name="Compra")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="itens_compra", verbose_name="Produto")
    quantidade = models.IntegerField("Quantidade")
    preco_unitario = models.DecimalField("Preço Unitário", max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"ItemCompra {self.id} da Compra {self.compra.id}"
    
    class Meta:
        db_table = "item_compra"
        verbose_name = "Item de Compra"
        verbose_name_plural = "Itens de Compra"
        ordering = ["compra", "produto"]

