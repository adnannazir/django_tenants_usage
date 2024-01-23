from django.db import models
from tenant_users.tenants.models import TenantBase, UserProfile
from django_tenants.models import DomainMixin


class User(UserProfile):
    name = models.CharField(max_length=100)


class Customer(TenantBase):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    # default true, schema will be automatically created and synced when it is saved
    # auto_create_schema = True

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass
