from zeroconf import Zeroconf

class MDNSScanner:

    def scan(self):

        zeroconf = Zeroconf()

        devices = []

        try:

            services = zeroconf.cache.entries()

            for service in services:

                devices.append({

                    "device_name": str(service),

                    "brand":"Unknown",

                    "connection_type":"mdns",

                })

        finally:

            zeroconf.close()

        return devices