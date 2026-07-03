from django import forms

from homes.models import Home
from rooms.models import Room


class PairDeviceForm(forms.Form):

    home = forms.ModelChoiceField(
        queryset=Home.objects.none()
    )

    room = forms.ModelChoiceField(
        queryset=Room.objects.none()
    )

    def __init__(self, *args, **kwargs):

        user = kwargs.pop("user")

        super().__init__(*args, **kwargs)

        self.fields["home"].queryset = Home.objects.filter(
            owner=user
        )

        self.fields["room"].queryset = Room.objects.filter(
            home__owner=user
        )