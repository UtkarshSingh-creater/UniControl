from django.urls import path

from . import views

urlpatterns = [

    path(
        "",
        views.discovered_devices,
        name="discovery",
    ),

    path(
        "scan/",
        views.scan_devices,
        name="scan_devices",
    ),

]