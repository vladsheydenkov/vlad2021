from django.contrib import admin
from . import models


@admin.register(models.Storage)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', )
