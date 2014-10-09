from django.db import models
from django.conf import settings
from tenant_schemas.models import TenantMixin

LEGAL_PERSON = 'PJ'
NATURAL_PERSON = 'PF'
ENTITY_CHOICES = (
    (LEGAL_PERSON, 'Legal Person'),
    (NATURAL_PERSON, 'Natural Person')
)


class Client(TenantMixin):
    name = models.CharField(max_length=180)
    entity = models.CharField(max_length=2, choices=ENTITY_CHOICES)
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    subdomain = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=180, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile_phone = models.CharField(max_length=20, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __unicode__(self):
        return self.name

    def save(self):
        host = settings.ALLOWED_HOSTS[0]
        if self.subdomain == 'public':
            self.domain_url = host
            self.schema_name = 'public'
        else:
            self.domain_url = self.subdomain + '.' + host
            self.schema_name = self.subdomain
        return super(Client, self).save()
