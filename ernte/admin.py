from django.contrib import admin

# Register your models here.

from . import models

class WarenlieferungInline(admin.TabularInline):
    model = models.Warenlieferung

class LieferungAdmin(admin.ModelAdmin):
    inlines = [
        WarenlieferungInline,
    ]

admin.site.register(models.Gruppe)
admin.site.register(models.Person)
admin.site.register(models.Ernteanteil)
admin.site.register(models.Abholstelle)
admin.site.register(models.Lieferung, LieferungAdmin)
admin.site.register(models.Ware)

