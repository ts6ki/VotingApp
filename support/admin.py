from django.contrib import admin

from .models import SupportDepartment, Ticket

admin.site.register(Ticket)
admin.site.register(SupportDepartment)
