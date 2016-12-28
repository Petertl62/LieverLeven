from django.contrib import admin

from .models import Contact
from .forms import ModelContactForm


class ContactAdmin(admin.ModelAdmin):
    form = ModelContactForm

admin.site.register(Contact, ContactAdmin)
