from abc import ABC, abstractmethod


class BluetoothBaseScanner(ABC):

    @abstractmethod
    def scan(self):
        pass