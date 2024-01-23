from django.contrib import admin
from accounts.models import User
from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Customer

# Register your models here.

admin.site.register(User)


@admin.register(Customer)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'code')
