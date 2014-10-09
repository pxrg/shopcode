from django.conf import settings
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from core.models import Client


class HomeView(CreateView):
    model = Client
    template_name = 'index.html'
    success_url = reverse_lazy('core:home')

    fields = ('name', 'entity', 'cpf_cnpj',
              'subdomain', 'email', 'phone',
              'mobile_phone')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['domain_url'] = settings.ALLOWED_HOSTS[0]
        return context
