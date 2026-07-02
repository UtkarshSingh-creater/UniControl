from django.db import models
from homes.models import Home

class Room(models.Model):
    home=models.ForeignKey(
        Home,
        on_delete=models.CASCADE,
        related_name="rooms"
    )

    name=models.CharField(max_length=100)
    floor=models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.name