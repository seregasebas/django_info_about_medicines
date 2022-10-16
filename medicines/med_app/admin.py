from django.contrib import admin
from .models import DrugName, DrugGroup, DrugManufacturer, Contacts
# Register your models here.

admin.site.register(DrugName)
admin.site.register(DrugGroup)
admin.site.register(DrugManufacturer)
admin.site.register(Contacts)
