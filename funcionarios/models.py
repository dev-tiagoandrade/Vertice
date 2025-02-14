from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.db import models

from Vertice import settings
from core.models import BaseModel, CHOICE


class Operador(AbstractUser, BaseModel):
    matricula = models.CharField("Matrícula", max_length=20, unique=True)
    cpf_operador = models.CharField("CPF do Operador", max_length=255, unique=True)
    biometria = models.BinaryField("Biometria", null=True, blank=True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = "operador"
        verbose_name = "Operador"
        verbose_name_plural = "Operadores"


class RegistroPonto(BaseModel):
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE, verbose_name="Operador")
    dt_ponto = models.DateTimeField("Data do Ponto", auto_now_add=True)
    tp_ponto = models.PositiveSmallIntegerField("Tipo de Ponto", choices=CHOICE.TIPO_REGISTRO_PONTO)
    observacao = models.CharField("Observação", max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f"RegistroPonto {self.id} - {self.operador.username}"
    
    class Meta:
        db_table = "registro_ponto"
        verbose_name = "Registro de Ponto"
        verbose_name_plural = "Registros de Ponto"
        ordering = ["-dt_ponto"]
        

class Auditoria(BaseModel):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Autor")
    autor_repr = models.CharField("Representação do Autor", max_length=200, null=True, blank=True, editable=False)
    ip_endereco = models.GenericIPAddressField("Endereço IP", editable=False)
    dt_registro = models.DateTimeField("Data do Registro", auto_now_add=True, editable=False)
    tipo_objeto = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tipo do Objeto")
    tipo_objeto_repr = models.CharField("Representação do Tipo de Objeto", max_length=200, null=True, blank=True, editable=False)
    objeto_id = models.PositiveIntegerField("ID do Objeto", null=True, blank=True, editable=False)
    objeto_repr = models.CharField("Representação do Objeto", max_length=200, null=True, blank=True, editable=False)
    tipo = models.PositiveIntegerField("Tipo de Ação", choices=CHOICE.ACAO_AUDITORIA, editable=False)
    observacoes = models.TextField("Observações", blank=True)
    alteracao = models.TextField("Detalhes da Alteração", blank=True)

    def __str__(self):
        return f"{self.dt_registro} - {self.tipo_objeto_repr}"

    class Meta:
        db_table = "auditoria"
        verbose_name = "Auditoria"
        verbose_name_plural = "Auditorias"
        ordering = ["-dt_registro"]