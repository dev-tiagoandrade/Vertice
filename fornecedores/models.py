from django.db import models
from core.models import BaseModel


class Fornecedor(BaseModel):
    nm_fornecedor = models.CharField("Nome do Fornecedor", max_length=255, db_index=True)
    cnpj_fornecedor = models.CharField("CNPJ do Fornecedor", max_length=20, unique=True)
    tel_fornecedor = models.CharField("Telefone do Fornecedor", max_length=20)
    email_fornecedor = models.EmailField("E-mail do Fornecedor", max_length=255)

    def __str__(self):
        return self.nm_fornecedor

    class Meta:
        db_table = "fornecedor"
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
        ordering = ["nm_fornecedor"]


