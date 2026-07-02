from django.db import models
from devices.models import Device


class Schedule(models.Model):

    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name="schedules"
    )

    action = models.CharField(max_length=100)

    run_at = models.DateTimeField()

    repeat = models.BooleanField(default=False)

    enabled = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device.name} - {self.action}"