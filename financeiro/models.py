# financeiro/models.py
from django.db import models
from core.models import BaseModel


class Caixa(BaseModel):
    dt_fechamento = models.DateField("Data de Fechamento")
    total_vendas = models.DecimalField("Total de Vendas", max_digits=10, decimal_places=2)
    total_pagamentos = models.DecimalField("Total de Pagamentos", max_digits=10, decimal_places=2)
    fluxo_caixa = models.DecimalField("Fluxo de Caixa", max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Caixa - {self.dt_fechamento}"
    
    class Meta:
        db_table = "caixa"
        verbose_name = "Caixa"
        verbose_name_plural = "Caixas"
        ordering = ["-dt_fechamento"]

