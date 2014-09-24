from django.views.generic.edit import CreateView
from core.models import Client


class RegisterClientView(CreateView):
    model = Client
    fields = ['name', 'email', 'domain_url']
    success_url = '/'

    def form_valid(self, form):
        domain_url = form.cleaned_data['domain_url']
        form.instance.schema_name = domain_url.split('.')[0]
        return super(RegisterClientView, self).form_valid(form)
