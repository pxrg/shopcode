from django.db import models
from tenant_schemas.models import TenantMixin


class Client(TenantMixin):
    description = models.TextField(max_length=200)
    created_on = models.DateField(auto_now_add=True)
    user = models.ForeignKey('auth.User')
