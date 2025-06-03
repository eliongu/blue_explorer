import network
import espnow


sta = network.WLAN(network.WLAN.IF_STA)
sta.active(True)
sta.disconnect()

e = espnow.ESPNow()
e.active(True)

while True:
    host, msg = e.recv()
    if msg:             
        print(host, msg)
        if msg == b'end':
            break