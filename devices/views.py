import asyncio

from .services.bluetooth_status import BluetoothStatusChecker
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import ConnectedDevice
from .forms import ConnectedDeviceForm
from discovery.models import DiscoveredDevice
from .pair_forms import PairDeviceForm

@login_required
def device_list(request):

    try:

        status = BluetoothStatusChecker.scan()

        devices = ConnectedDevice.objects.filter(
            home__owner=request.user
        ).select_related(
            "home",
            "room",
        )

        for device in devices:

            if device.connection_type == "bluetooth":

                if device.mac_address:

                    device.online = status.get(
                        device.mac_address.upper(),
                        False,
                    )

                    device.save(update_fields=["online"])

    except Exception as e:

        print("Bluetooth status check failed:", e)

        devices = ConnectedDevice.objects.filter(
            home__owner=request.user
        ).select_related(
            "home",
            "room",
        )

    return render(
        request,
        "devices/device_list.html",
        {
            "devices": devices,
        },
    )
    
@login_required
def device_create(request):

    if request.method == "POST":

        form = ConnectedDeviceForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("device_list")

    else:

        form = ConnectedDeviceForm()

    return render(
        request,
        "devices/device_form.html",
        {
            "form": form,
        },
    )


@login_required
def device_update(request, pk):

    device = get_object_or_404(
        ConnectedDevice,
        pk=pk,
        home__owner=request.user,
    )

    if request.method == "POST":

        form = ConnectedDeviceForm(
            request.POST,
            instance=device,
        )

        if form.is_valid():

            form.save()

            return redirect("device_list")

    else:

        form = ConnectedDeviceForm(
            instance=device,
        )

    return render(
        request,
        "devices/device_form.html",
        {
            "form": form,
        },
    )


@login_required
def device_delete(request, pk):

    device = get_object_or_404(
        ConnectedDevice,
        pk=pk,
        home__owner=request.user,
    )

    if request.method == "POST":

        device.delete()

        return redirect("device_list")

    return render(
        request,
        "devices/device_delete.html",
        {
            "device": device,
        },
    )


@login_required
def pair_device(request, pk):

    discovered = get_object_or_404(
        DiscoveredDevice,
        pk=pk,
    )

    if request.method == "POST":

        form = PairDeviceForm(
            request.POST,
            user=request.user,
        )

        if form.is_valid():

            device, created = ConnectedDevice.objects.get_or_create(

                mac_address=discovered.mac_address,

                defaults={

                    "name": discovered.device_name,

                    "brand": discovered.brand,

                    "model": discovered.model,

                    "device_type": discovered.device_type,

                    "connection_type": discovered.connection_type,

                    "ip_address": discovered.ip_address,

                    "home": form.cleaned_data["home"],

                    "room": form.cleaned_data["room"],

                    "paired": True,

                    "online": discovered.online,

                },

            )

            if not created:

                device.name = discovered.device_name
                device.brand = discovered.brand
                device.model = discovered.model
                device.device_type = discovered.device_type
                device.connection_type = discovered.connection_type
                device.ip_address = discovered.ip_address
                device.home = form.cleaned_data["home"]
                device.room = form.cleaned_data["room"]
                device.paired = True
                device.online = discovered.online

                device.save()

            discovered.paired = True
            discovered.save()

            return redirect("device_list")

    else:

        form = PairDeviceForm(
            user=request.user,
        )

    return render(
        request,
        "devices/pair_device.html",
        {
            "device": discovered,
            "form": form,
        },
    )