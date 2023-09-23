from django.contrib import admin

from invoices.models import Invoice, InvoiceDetail

admin.site.register(Invoice)
admin.site.register(InvoiceDetail)
# Register your models here.
