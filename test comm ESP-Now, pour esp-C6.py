import network
import espnow


sta = network.WLAN(network.WLAN.IF_STA) 
sta.active(True)
sta.disconnect() 

e = espnow.ESPNow()
e.active(True)
macC3 = b'hg%\xe8w\xe4'
e.add_peer(macC3)  

e.send(macC3, "Starting...")
for i in range(100):
    e.send(macC3, str(i)*20, True)
e.send(macC3, b'end')