import network
w0 = network.WLAN(network.STA_IF)
w0.active(True)
print(w0.config('mac'))
