from django.contrib import admin
from .models import DiscoveredDevice


@admin.register(DiscoveredDevice)
class DiscoveredDeviceAdmin(admin.ModelAdmin):

    list_display = (
        "device_name",
        "brand",
        "device_type",
        "connection_type",
        "online",
        "paired",
    )

    search_fields = (
        "device_name",
        "brand",
        "ip_address",
    )