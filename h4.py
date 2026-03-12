from scapy.all import *
eth = Dot3(dst="01:80:c2:00:00:00", src="00:11:22:33:44:55")
llc_header = LLC(dsap=0x42, ssap=0x42, ctrl=3)
raw_data = "Merhaba, bu bir LLC cercevesidir!"
fake_frame = eth / llc_header / raw_data
print("--- Cerceve Detaylari ---")
fake_frame.show()

# sendp(fake_frame, iface="eth0")
