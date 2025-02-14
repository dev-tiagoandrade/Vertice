from django.views.generic import *
from .forms import *


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/produto_create.html'
    success_url = 'index'


class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/produto_create.html'
    success_url = 'index'

