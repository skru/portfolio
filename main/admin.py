from django.contrib import admin
from .models import *

class SectionImageInlineAdmin(admin.TabularInline):
    model = SectionImage

class SectionLinkInlineAdmin(admin.TabularInline):
    model = SectionLink

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
    inlines = [
        SectionImageInlineAdmin,
        SectionLinkInlineAdmin,
    ]
