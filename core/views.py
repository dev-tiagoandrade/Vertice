from django.views.generic import *


class Index(TemplateView):
    template_name = 'core/index.html'
