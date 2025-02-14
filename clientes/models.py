from django.db import models
from core.models import BaseModel


class Cliente(BaseModel):
    nm_cliente = models.CharField("Nome do Cliente", max_length=255, db_index=True)
    cpf_cliente = models.CharField("CPF do Cliente", max_length=14, unique=True, null=True, blank=True)
    tel_cliente = models.CharField("Telefone do Cliente", max_length=20)
    email_cliente = models.EmailField("E-mail do Cliente", max_length=255)
    limite_credito = models.DecimalField("Limite de Crédito", max_digits=10, decimal_places=2)
    saldo_fiado = models.DecimalField("Saldo Fiado", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nm_cliente

    class Meta:
        db_table = "cliente"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["nm_cliente"]

