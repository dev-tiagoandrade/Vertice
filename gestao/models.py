from django.contrib.auth.models import AbstractUser
from django.db import models


class CHOICES:
    TIPO_REGISTRO = (
        ('entrada', 'Entrada'),
        ('saida', 'Saída')
    )
    
    class Meta:
        abstract = True


class Cargo(models.Model):
    cargo = models
    
    class Meta:
        db_table = 'cargo'
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'


class Funcionario(AbstractUser):
    """
    Modelo customizado de usuário para representar os funcionários da empresa.
    Extende AbstractUser.
    """
    cpf_funcionario = models.CharField('CPF do Funcionário', max_length=14, unique=True)
    matricula_funcionario = models.CharField('Matrícula do Funcionário', max_length=8, unique=True)
    cargo = models.CharField('Cargo do Funcionário', max_length=100, blank=True, null=True)
    dt_admissao_funcionario = models.DateField('Data de Admissão do Funcionário', blank=True, null=True)
    tel_funcionario = models.CharField('Telefone do Funcionário', max_length=20, blank=True, null=True)
    funcionario_ativo = models.BooleanField('Ativo', default=True)
    
    img_funcionario = models.ImageField('Foto do Funcionário', upload_to='funcionarios/', blank=True, null=True)
    
    def __str__(self):
        nome_completo = self.get_full_name() or self.username
        return f"{nome_completo} - {self.cargo or 'Sem Cargo'}"
    
    class Meta:
        db_table = 'funcionario'
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'


class RegistroPonto(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    dt_registro = models.DateTimeField(auto_now_add=True, editable=False)
    tipo_registro = models.CharField('Típo de Registro', choices=CHOICES.TIPO_REGISTRO, max_length=10)
    
    class Meta:
        db_table = 'registro_ponto'
        verbose_name = 'Registro de Ponto'
        verbose_name_plural = 'Registro de Pontos'
