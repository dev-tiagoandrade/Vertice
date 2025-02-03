from django.db import models


class CHOICES:
    UNIDADE_MEDIDA = (
        ('unidade', 'Unidade'),
        ('quilo', 'Quilo'),
        ('litro', 'Litro'),
        ('metro', 'Metro')
    )
    
    class Meta:
        abstract = True


from django.db import models


# Possível modelo para Fornecedor, caso queira gerenciar essa informação
class Fornecedor(models.Model):
    nome = models.CharField('Nome do Fornecedor', max_length=255)
    cnpj = models.CharField('CNPJ', max_length=18, unique=True)
    contato = models.CharField('Contato', max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'fornecedor'
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'


# Modelo de Categoria para produtos
class Categoria(models.Model):
    nome = models.CharField('Nome da Categoria', max_length=100, unique=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


# Classe para Produtos
class Produto(models.Model):
    cdg_produto = models.CharField('Código do Produto', max_length=13, unique=True)
    nm_produto = models.CharField('Nome do Produto', max_length=255)
    desc_produto = models.TextField('Descrição do Produto', blank=True, null=True)
    preco_venda_produto = models.FloatField('Preço de Venda')
    preco_compra_produto = models.FloatField('Preço de Compra', blank=True, null=True)
    margem_lucro_produto = models.FloatField('Margem de Lucro (%)', blank=True, null=True)
    
    # Dados de fabricação e validade
    fabricante_produto = models.CharField('Fabricante do Produto', max_length=255, null=True, blank=True)
    lt_produto = models.CharField('Lote do Produto', max_length=13, blank=True, null=True)
    dt_fbr_produto = models.DateTimeField('Data de Fabricação do Produto', blank=True, null=True)
    dt_val_produto = models.DateTimeField('Data de Validade do Produto', blank=True, null=True)
    
    # Informações para controle do produto no sistema
    ativo_produto = models.BooleanField('Produto Ativo', default=True)
    img_produto = models.ImageField('Imagem do Produto', upload_to='produtos/', blank=True, null=True)
    
    # Relacionamentos
    ctg_produto = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    fornecedor_produto = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Unidade de Medida
    md_produto = models.CharField(
        'Unidade de Medida',
        max_length=10,
        choices=CHOICES.UNIDADE_MEDIDA,
        default='unidade'
    )
    
    # Campos para produtos vendidos a quilo
    ps_liquido_produto = models.FloatField('Peso Líquido (kg)', blank=True, null=True)
    ps_bruto_produto = models.FloatField('Peso Bruto (kg)', blank=True, null=True)
    
    def __str__(self):
        return f'{self.nm_produto} ({self.cdg_produto})'
    
    class Meta:
        db_table = 'produto'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


# Classe para Produtos em Estoque
class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtd_estoque = models.FloatField('Quantidade em Estoque')
    estoque_minimo = models.FloatField('Estoque Mínimo', default=0)
    
    dt_entrada_estoque = models.DateTimeField('Data de Entrada no Estoque', auto_now_add=True)
    dt_atualiza_estoque = models.DateTimeField('Data de Atualização do Estoque', auto_now=True)
    
    def __str__(self):
        return f'{self.qtd_estoque} {self.produto.unidade_medida}(s) de {self.produto}'
    
    class Meta:
        db_table = 'estoque'
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'


