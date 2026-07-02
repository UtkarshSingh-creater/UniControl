from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from devices.models import Device
from homes.models import Home
from rooms.models import Room
from automation.models import Automation
from notifications.models import Notification


@login_required(login_url="login")
def dashboard(request):

    total_devices = Device.objects.count()

    online_devices = Device.objects.filter(
        is_online=True
    ).count()

    offline_devices = Device.objects.filter(
        is_online=False
    ).count()

    total_homes = Home.objects.count()

    total_rooms = Room.objects.count()

    total_automations = Automation.objects.count()

    recent_notifications = Notification.objects.filter(
        user=request.user
    ).order_by("-created_at")[:5]

    context = {
        "total_devices": total_devices,
        "online_devices": online_devices,
        "offline_devices": offline_devices,
        "total_homes": total_homes,
        "total_rooms": total_rooms,
        "total_automations": total_automations,
        "recent_notifications": recent_notifications,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )