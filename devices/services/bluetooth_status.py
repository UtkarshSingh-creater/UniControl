import subprocess
import re


class BluetoothStatusChecker:

    @staticmethod
    def scan():

        result = subprocess.run(
            ["bluetoothctl", "devices"],
            capture_output=True,
            text=True,
        )

        status = {}

        for line in result.stdout.splitlines():

            match = re.match(
                r"Device\s+([0-9A-F:]+)",
                line,
            )

            if not match:
                continue

            mac = match.group(1).upper()

            info = subprocess.run(
                ["bluetoothctl", "info", mac],
                capture_output=True,
                text=True,
            )

            connected = "Connected: yes" in info.stdout

            status[mac] = connected

        return status