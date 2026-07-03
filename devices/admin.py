from django.contrib import admin

from .models import ConnectedDevice


@admin.register(ConnectedDevice)
class ConnectedDeviceAdmin(admin.ModelAdmin):

    list_display = (

        "name",

        "brand",

        "device_type",

        "connection_type",

        "home",

        "room",

        "paired",

        "online",

    )

    list_filter = (

        "connection_type",

        "device_type",

        "paired",

        "online",

    )

    search_fields = (

        "name",

        "brand",

        "model",

        "mac_address",

    )