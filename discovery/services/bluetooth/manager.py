from .classic import ClassicBluetoothScanner
from .ble import BLEScanner


class BluetoothScanner:

    def __init__(self):

        self.scanners = [

            ClassicBluetoothScanner(),

            BLEScanner(),

        ]

    def scan(self):

        devices = []

        for scanner in self.scanners:

            devices.extend(scanner.scan())

        return devices