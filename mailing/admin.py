from django.contrib import admin

from .models import ContactData


@admin.register(ContactData)
class ContactDataAdmin(admin.ModelAdmin):
    list_display = ('email', 'datetime')
