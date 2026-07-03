import subprocess
import re

from .base import BluetoothBaseScanner


class ClassicBluetoothScanner(BluetoothBaseScanner):

    def scan(self):

        devices = []

        try:

            result = subprocess.run(

                ["bluetoothctl", "devices"],

                capture_output=True,

                text=True,

            )

            output = result.stdout.splitlines()

            for line in output:

                match = re.match(
                    r"Device\s+([0-9A-F:]+)\s+(.*)",
                    line
                )

                if match:

                    mac = match.group(1)

                    name = match.group(2)

                    devices.append({

                        "device_name": name if name else "Unknown Device",

                        "brand": "Bluetooth",

                        "model": "",

                        "device_type": "Classic Bluetooth",

                        "connection_type": "bluetooth",

                        "ip_address": None,

                        "mac_address": mac,

                        "paired": False,

                        "online": True,

                    })

        except Exception as e:

            print(e)

        return devices