from django.contrib import admin

# Register your models here.

from .models import Note_Type,Notes

# Register your models here.
@admin.register(Notes,Note_Type)
class DefaultAdmin(admin.ModelAdmin):
    pass
