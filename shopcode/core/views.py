from core.models import Client
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse_lazy
from django.db import connection
from django.views.generic.edit import CreateView
from tenant_schemas.utils import get_tenant_model


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

    def form_valid(self, form):
        self.object = form.save()
        # tenant set schema create
        TenantModel = get_tenant_model()
        tenant = TenantModel.objects.get(domain_url=self.object.domain_url)
        connection.set_tenant(tenant)
        ContentType.objects.clear_cache()
        # create user
        username = self.object.cpf_cnpj
        email = User.objects.normalize_email(self.object.email)
        password = User.objects.make_random_password(length=10)
        User.objects.create_superuser(username, email, password)
        # envia e-mail
        self.send_mail(email, username, password)
        return super(HomeView, self).form_valid(form)

    def send_mail(self, to, user, password):
        from_email = 'igr.exe@gmail.com'
        subject = 'Password SaaS.io System'
        text = 'This is usernae {0} and password {0}.'.format(user, password)
        html = '<p>This is password <strong>{0}</strong>.</p>'.format(password)
        msg = EmailMultiAlternatives(subject, text, from_email, [to])
        msg.attach_alternative(html, "text/html")
        msg.send()
