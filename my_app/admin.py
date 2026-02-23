from django.contrib import admin
from .models import Author


@admin.register(Author)
class AthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
