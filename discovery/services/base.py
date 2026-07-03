from abc import ABC, abstractmethod


class BaseScanner(ABC):
    """
    Base class for all discovery scanners.
    """

    @abstractmethod
    def scan(self):
        """
        Returns:
            List[dict]
        """
        pass