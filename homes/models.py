from django.db import models
from django.conf import settings

class Home(models.Model):
    owner=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="homes"
    )

    name=models.CharField(max_length=100)
    address=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name