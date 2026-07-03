import logging

from .bluetooth.manager import BluetoothScanner
from .ssdp import SSDPScanner
from .mdns import MDNSScanner
from .storage import DiscoveryStorage


logger = logging.getLogger(__name__)


class DiscoveryManager:
    """
    Central Discovery Manager.

    Responsibilities:
    - Run all registered scanners
    - Merge results
    - Remove duplicate devices
    - Save devices to the database
    """

    def __init__(self):

        self.scanners = [
            BluetoothScanner(),
            SSDPScanner(),
            MDNSScanner(),
        ]

        self.storage = DiscoveryStorage()

    def scan(self):

        discovered_devices = []

        for scanner in self.scanners:

            logger.info(
                "Running %s...",
                scanner.__class__.__name__,
            )

            try:

                devices = scanner.scan()

                if devices:
                    discovered_devices.extend(devices)

                    logger.info(
                        "%s discovered %d device(s).",
                        scanner.__class__.__name__,
                        len(devices),
                    )

            except Exception:

                logger.exception(
                    "%s failed.",
                    scanner.__class__.__name__,
                )

        discovered_devices = self.remove_duplicates(
            discovered_devices
        )

        if discovered_devices:
            self.storage.save(discovered_devices)

        logger.info(
            "Total unique devices discovered: %d",
            len(discovered_devices),
        )

        return discovered_devices

    @staticmethod
    def remove_duplicates(devices):

        unique = {}

        for device in devices:

            key = (
                device.get("mac_address")
                or device.get("ip_address")
                or device.get("device_name")
            )

            if key:
                unique[key] = device

        return list(unique.values())