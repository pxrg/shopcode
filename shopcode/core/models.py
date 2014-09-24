from django.db import models
from tenant_schemas.models import TenantMixin


class Client(TenantMixin):
    name = models.CharField(max_length=180)
    email = models.EmailField(max_length=180)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __unicode__(self):
        return self.name
