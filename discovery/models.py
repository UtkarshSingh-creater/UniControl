from django.db import models


class DiscoveredDevice(models.Model):

    CONNECTION_TYPES = [
        ("wifi", "Wi-Fi"),
        ("bluetooth", "Bluetooth"),
        ("mdns", "mDNS"),
        ("ssdp", "SSDP"),
        ("matter", "Matter"),
    ]

    device_name = models.CharField(max_length=150)

    brand = models.CharField(
        max_length=100,
        blank=True,
        default="Unknown",
    )

    model = models.CharField(
        max_length=100,
        blank=True,
    )

    device_type = models.CharField(
        max_length=100,
        default="Unknown",
    )

    ip_address = models.GenericIPAddressField(
        blank=True,
        null=True,
    )

    mac_address = models.CharField(
        max_length=50,
        blank=True,
        unique=True,
        null=True,
    )

    connection_type = models.CharField(
        max_length=30,
        choices=CONNECTION_TYPES,
    )

    paired = models.BooleanField(default=False)

    online = models.BooleanField(default=True)

    discovered_at = models.DateTimeField(
        auto_now_add=True,
    )

    last_seen = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-last_seen"]

    def __str__(self):
        return self.device_name