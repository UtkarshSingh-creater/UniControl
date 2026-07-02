from django.db import models
from rooms.models import Room
from integrations.models import Integration

class DeviceType(models.Model):
    
    name=models.CharField(max_length=100,unique=True)

    icon=models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Device(models.Model):

    CONNECTION_TYPES = [
        ("wifi", "Wi-Fi"),
        ("bluetooth", "Bluetooth"),
        ("mqtt", "MQTT"),
        ("matter", "Matter"),
        ("zigbee", "Zigbee"),
        ("zwave", "Z-Wave"),
    ]

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="devices"
    )

    device_type = models.ForeignKey(
        DeviceType,
        on_delete=models.CASCADE
    )

    integration = models.ForeignKey(
        Integration,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)

    brand = models.CharField(max_length=100)

    model = models.CharField(max_length=100)

    connection_type = models.CharField(
        max_length=20,
        choices=CONNECTION_TYPES
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True
    )

    mac_address = models.CharField(
        max_length=17,
        blank=True
    )

    firmware_version = models.CharField(
        max_length=50,
        blank=True
    )

    serial_number = models.CharField(
        max_length=100,
        blank=True
    )

    is_online = models.BooleanField(default=False)

    last_seen = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class DeviceCapability(models.Model):

    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name="capabilities"
    )

    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.device.name} - {self.name}"


class DeviceState(models.Model):

    device = models.OneToOneField(
        Device,
        on_delete=models.CASCADE,
        related_name="state"
    )

    state = models.JSONField(default=dict)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device.name