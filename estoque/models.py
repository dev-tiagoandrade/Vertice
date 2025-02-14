from django.db import models
from core.models import BaseModel
from produtos.models import Produto


class Estoque(BaseModel):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="estoques", verbose_name="Produto")
    qtd_estoque = models.DecimalField("Quantidade em Estoque", max_digits=10, decimal_places=2)
    localizacao = models.CharField("Localização", max_length=255)
    atualizacao = models.DateTimeField("Última Atualização", auto_now=True)
    
    def __str__(self):
        return f"Estoque de {self.produto.nm_produto}"
    
    class Meta:
        db_table = "estoque"
        verbose_name = "Estoque"
        verbose_name_plural = "Estoques"
        ordering = ["produto__nm_produto"]
