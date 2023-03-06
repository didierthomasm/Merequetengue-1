from django.contrib import admin

from Fandango.models import Pegoste


class PegosteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Pegoste, PegosteAdmin)
