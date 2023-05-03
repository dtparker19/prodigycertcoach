from django.db import models
from tenant_schemas.models import TenantMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    on_trial = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True

    def __str__(self):
        return self.name


class Language(TenantMixin):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
