from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .services.manager import DiscoveryManager
from .models import DiscoveredDevice


@login_required
def scan_devices(request):
    """
    Scan the local network for smart devices.
    """

    manager = DiscoveryManager()

    manager.scan()

    devices = DiscoveredDevice.objects.all().order_by(
        "-last_seen"
    )

    return render(
        request,
        "discovery/scan.html",
        {
            "devices": devices,
        },
    )


@login_required
def discovered_devices(request):
    """
    Show previously discovered devices.
    """

    devices = DiscoveredDevice.objects.all().order_by(
        "-last_seen"
    )

    return render(
        request,
        "discovery/scan.html",
        {
            "devices": devices,
        },
    )