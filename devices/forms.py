from django import forms

from .models import ConnectedDevice


class ConnectedDeviceForm(forms.ModelForm):

    class Meta:

        model = ConnectedDevice

        fields = [

            "name",

            "brand",

            "model",

            "device_type",

            "connection_type",

            "home",

            "room",

        ]