from django.db import models
from django.conf import settings

from devices.models import ConnectedDevice


class DeviceLog(models.Model):

    STATUS = [

        ("success", "Success"),

        ("failed", "Failed"),

    ]

    device = models.ForeignKey(

        ConnectedDevice,

        on_delete=models.CASCADE,

        related_name="logs",

    )

    user = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

    )

    action = models.CharField(max_length=100)

    response = models.TextField(blank=True)

    status = models.CharField(

        max_length=20,

        choices=STATUS,

        default="success",

    )

    created_at = models.DateTimeField(

        auto_now_add=True,

    )

    def __str__(self):

        return f"{self.device.name} - {self.action}"