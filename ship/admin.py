from django.contrib import admin
from ship.models import Package
from ship.models import Recipient

class PackageInline(admin.TabularInline):
    model = Package
    extra =0

class PackageAdmin(admin.ModelAdmin):
    inlines = [PackageInline]
    list_display = ['recip_username','recip_first_name', 'recip_last_name', 'recip_n_packages']

admin.site.register(Recipient, PackageAdmin)
admin.site.register(Package)




