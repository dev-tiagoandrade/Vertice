from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField("Data de Criação", auto_now_add=True)
    ativo = models.BooleanField("Ativo", default=True)

    class Meta:
        abstract = True


class CHOICE:
    UNIDADE_MEDIDA = [
        (0, "Unidade"),
        (1, "Quilo"),
        (2, "Litro"),
        (3, "Metro"),
        (4, "Atacado"),
    ]

    METODO_PAGAMENTO = [
        (0, "Dinheiro"),
        (1, "Débito"),
        (2, "Crédito"),
        (3, "Vale"),
        (4, "PIX"),
    ]

    STATUS_PAGAMENTO = [
        (0, "Pendente"),
        (1, "Concluído"),
        (2, "Falha"),
    ]

    STATUS_COMPRA = [
        (1, "Pendente"),
        (2, "Concluído"),
        (3, "Em Processamento"),
    ]

    TIPO_REGISTRO_PONTO = [
        (0, "Entrada"),
        (1, "Saída"),
        (2, "Intervalo"),
    ]

    ACAO_AUDITORIA = [
        (0, "Logout"),
        (1, "Login"),
        (2, "Criação"),
        (3, "Alteração"),
        (4, "Deleção"),
    ]

