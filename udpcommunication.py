Things to do after downloading

1) Unzip and get the folder
2) Openthonny
3) Find the folder directory you just unzipped on your local computer in the upper right corner
4) Select 5a .pyfile, right-click and upload to/
5) At this point, you will see that 5 files have been transferred to esp32 in the lower right corner.

The installation is complete...

test_code.py

from wiznet5k import WIZNET5K
from machine import Pin, SPI
import wiznet5k_socket as socket
import sma_esp32_w5500_requests as requests
import time

spi = SPI(2)
cs = Pin(5,Pin.OUT)
rst=Pin(34)
nic = WIZNET5K(spi,cs,rst)

print("\n\n以太网芯片版本:", nic.chip)
print("网卡MAC地址:", [hex(i) for i in nic.mac_address])
print("IP地址:", nic.pretty_ip(nic.ip_address))

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest_addr = ('192.168.31.53', 8080)

for i in range(10):
    send_data = "hello world--%d" % i
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
    time.sleep(1)

udp_socket.close()
