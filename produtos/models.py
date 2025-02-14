from django.db import models
from core.models import BaseModel, CHOICE
from fornecedores.models import Fornecedor


class Produto(BaseModel):
    nm_produto = models.CharField("Nome do Produto", max_length=255, db_index=True)
    cdg_produto = models.CharField("Código do Produto", max_length=50, unique=True)
    dsc_produto = models.TextField("Descrição do Produto")
    preco_venda = models.DecimalField("Preço de Venda", max_digits=10, decimal_places=2)
    preco_compra = models.DecimalField("Preço de Compra", max_digits=10, decimal_places=2)
    margem_lucro = models.DecimalField("Margem de Lucro (%)", max_digits=5, decimal_places=2)
    estoque_atual = models.DecimalField("Estoque Atual", max_digits=10, decimal_places=2)
    estoque_minimo = models.DecimalField("Estoque Mínimo", max_digits=10, decimal_places=2)
    und_medida = models.PositiveSmallIntegerField("Unidade de Medida", choices=CHOICE.UNIDADE_MEDIDA)
    venda_por_peso = models.BooleanField("Venda por Peso", default=False)
    dt_validade = models.DateField("Data de Validade", null=True, blank=True)
    tp_produto = models.CharField("Tipo de Produto", max_length=2)
    peso_bruto = models.DecimalField("Peso Bruto", max_digits=10, decimal_places=2, null=True, blank=True)
    peso_liquido = models.DecimalField("Peso Líquido", max_digits=10, decimal_places=2, null=True, blank=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name="produtos", verbose_name="Fornecedor")

    def __str__(self):
        return self.nm_produto

    class Meta:
        db_table = "produto"
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["nm_produto"]
    
    
class Promocao(BaseModel):
    nm_promocao = models.CharField("Nome da Promoção", max_length=255, db_index=True)
    dsc_promocao = models.TextField("Descrição da Promoção")
    tipo = models.CharField("Tipo de Promoção", max_length=50)
    dt_inicio = models.DateTimeField("Data de Início")
    dt_fim = models.DateTimeField("Data de Término")
    
    def __str__(self):
        return self.nm_promocao
    
    class Meta:
        db_table = "promocao"
        verbose_name = "Promoção"
        verbose_name_plural = "Promoções"
        ordering = ["-dt_inicio"]


