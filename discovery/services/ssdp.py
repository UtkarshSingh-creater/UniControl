import socket
import re

class SSDPScanner:

    MSEARCH = "\r\n".join([
        "M-SEARCH * HTTP/1.1",
        "HOST:239.255.255.250:1900",
        'MAN:"ssdp:discover"',
        "MX:2",
        "ST:ssdp:all",
        "",
        ""
    ])

    def scan(self):

        devices = []

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.settimeout(3)

        sock.sendto(
            self.MSEARCH.encode(),
            ("239.255.255.250",1900)
        )

        while True:

            try:

                data, addr = sock.recvfrom(65535)

                text = data.decode(errors="ignore")

                server = ""

                location = ""

                if "SERVER:" in text:

                    server = re.findall(
                        r"SERVER:(.*)",
                        text,
                        re.IGNORECASE
                    )[0].strip()

                if "LOCATION:" in text:

                    location = re.findall(
                        r"LOCATION:(.*)",
                        text,
                        re.IGNORECASE
                    )[0].strip()

                devices.append({

                    "device_name": addr[0],

                    "brand": server,

                    "ip_address": addr[0],

                    "device_type":"Unknown",

                    "connection_type":"wifi",

                    "location":location,

                })

            except socket.timeout:

                break

        sock.close()

        return devices