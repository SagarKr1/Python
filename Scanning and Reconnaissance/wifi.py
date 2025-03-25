import subprocess
import re

wifi = subprocess.run(["ipconfig"], shell=True, capture_output=True, text=True)

wifiDetails = wifi.stdout
# print(wifiDetails)
wifi_section = wifiDetails.split("Wireless LAN adapter Wi-Fi")[1] if "Wireless LAN adapter Wi-Fi" in wifiDetails else ""
if not wifi_section:
    print("No Data Dound")
else:
    ipAddress = re.findall(r"IPv4 Address[ .:]+([\d.]+)",wifi_section)
    subnet = re.findall(r"Subnet Mask[ .:]+([\d.]+)",wifi_section)
    data = {
        "Ip Address":ipAddress,
        "Subnet":subnet
    }
    print(data)
