import network
import espnow
from machine import ADC, Pin
import time

sta = network.WLAN(network.WLAN.IF_STA)
sta.active(True)
sta.disconnect()

e = espnow.ESPNow()
e.active(True)


macC6 = b'@L\xcaV\xbe,'
e.add_peer(macC6)

# Joystick
vrx = ADC(Pin(3))  # Axe X
vry = ADC(Pin(0))  # Axe Y

vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)

sw = Pin(1, Pin.IN, Pin.PULL_UP)

# Constantes
DEAD_ZONE = 200  # zone morte pour éviter les variations
CENTER = 2400

def get_direction(x, y):
    if abs(x - CENTER) < DEAD_ZONE and abs(y - CENTER) < DEAD_ZONE:
        return "CENTRE"
    if y < CENTER - DEAD_ZONE:
        return "HAUT"
    if y > CENTER + DEAD_ZONE:
        return "BAS"
    if x < CENTER - DEAD_ZONE:
        return "GAUCHE"
    if x > CENTER + DEAD_ZONE:
        return "DROITE"
    return "?"

while True:
    x = vrx.read()
    y = vry.read()
    sw_val = sw.value()
    direction = get_direction(x, y)
    bouton = "pressé" if sw_val == 0 else "relâché"

    
    message = direction + "|" + bouton  

    print("Envoi:", message)
    e.send(macC6, message)
    time.sleep(0.3)
