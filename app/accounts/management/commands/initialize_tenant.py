from django.core.management.base import BaseCommand

from accounts.models import Customer, User
from tenant_users.tenants.tasks import provision_tenant
from tenant_users.tenants.utils import create_public_tenant


class Command(BaseCommand):
    help = "Initialize tenant"

    def handle(self, *args, **kwargs):
        # create your public tenant
        if Customer.objects.filter(schema_name="public").first():
            return

        create_public_tenant(domain_url="localhost", owner_email="adnan@codevstan.com", tenant_extra_data={"code": "public"})

        self.stdout.write(self.style.SUCCESS('Default Tenant created successfully.'))

        User.objects.create_user("ad@codevstan.com", "A1234", True)

        provision_tenant("demo1", "demo", "ad@codevstan.com", tenant_extra_data={"code": "demo"})
        self.stdout.write(self.style.SUCCESS('demo Tenant created successfully.'))
