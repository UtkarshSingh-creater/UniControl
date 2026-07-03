from django.db import models

from homes.models import Home
from rooms.models import Room


class ConnectedDevice(models.Model):

    CONNECTION_TYPES = [
        ("bluetooth", "Bluetooth"),
        ("wifi", "WiFi"),
        ("matter", "Matter"),
        ("mqtt", "MQTT"),
    ]

    DEVICE_TYPES = [
        ("tv", "TV"),
        ("speaker", "Speaker"),
        ("light", "Smart Light"),
        ("fan", "Smart Fan"),
        ("ac", "Air Conditioner"),
        ("plug", "Smart Plug"),
        ("phone", "Phone"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=150)

    brand = models.CharField(
        max_length=100,
        blank=True
    )

    model = models.CharField(
        max_length=100,
        blank=True
    )

    device_type = models.CharField(
        max_length=30,
        choices=DEVICE_TYPES,
        default="other"
    )

    connection_type = models.CharField(
        max_length=20,
        choices=CONNECTION_TYPES,
    )

    mac_address = models.CharField(
        max_length=50,
        blank=True,
        unique=True,
        null=True,
    )

    ip_address = models.GenericIPAddressField(
        blank=True,
        null=True,
    )

    home = models.ForeignKey(
        Home,
        on_delete=models.CASCADE,
        related_name="devices",
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="devices",
    )

    paired = models.BooleanField(default=False)

    connected = models.BooleanField(default=False)

    online = models.BooleanField(default=False)

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):

        return self.name