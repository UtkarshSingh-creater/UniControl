from django.db import models


class Automation(models.Model):

    name = models.CharField(max_length=100)

    trigger = models.TextField()

    action = models.TextField()

    enabled = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name