# -*- coding: utf-8 -*-
from django.contrib import admin
from core.models import Page, InfoBlock, Photo, SocialContacts, Contacts


class SocialInlinesAdmin(admin.StackedInline):
    model = SocialContacts


class ContactsAdmin(admin.ModelAdmin):
    inlines = [ SocialInlinesAdmin, ]


admin.site.register(Page)
admin.site.register(InfoBlock)
admin.site.register(Photo)
admin.site.register(Contacts, ContactsAdmin)
