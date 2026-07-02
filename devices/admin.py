from django.contrib import admin
from .models import DeviceType,DeviceCapability,Device,DeviceState

admin.site.register(DeviceType)
admin.site.register(Device)
admin.site.register(DeviceCapability)
admin.site.register(DeviceState)