from discovery.models import DiscoveredDevice


class DiscoveryStorage:

    def save(self, devices):

        for device in devices:

            lookup = {}

            if device.get("mac_address"):

                lookup["mac_address"] = device["mac_address"]

            elif device.get("ip_address"):

                lookup["ip_address"] = device["ip_address"]

            else:

                lookup["device_name"] = device["device_name"]

            defaults = {

                "device_name": device.get("device_name", ""),

                "brand": device.get("brand", "Unknown"),

                "model": device.get("model", ""),

                "device_type": device.get("device_type", ""),

                "ip_address": device.get("ip_address"),

                "mac_address": device.get("mac_address", ""),

                "connection_type": device.get(
                    "connection_type",
                    "wifi",
                ),

                "paired": device.get("paired", False),

                "online": device.get("online", True),

            }

            DiscoveredDevice.objects.update_or_create(

                defaults=defaults,

                **lookup,

            )