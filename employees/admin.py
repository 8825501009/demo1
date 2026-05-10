from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Department, Policy, Contact

admin.site.register(Department)
admin.site.register(Policy)
admin.site.register(Contact)