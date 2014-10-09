from django.core.management.base import BaseCommand
from core.models import Client


class Command(BaseCommand):

    def handle(self, **options):
        tenant = Client(
            name='Master App.', entity='PF',
            subdomain='public', cpf_cnpj='11111111111',
            email='root@root.com'
        )
        tenant.save()
        print 'Ok, created a public schema!'
