import network
import espnow
from machine import ADC, Pin
import time

# LEDs
greenled = Pin(5, Pin.OUT)
redled = Pin(4, Pin.OUT)

# ESP-NOW
sta = network.WLAN(network.WLAN.IF_STA)
sta.active(True)
sta.disconnect()

# Initialisation ESP-NOW
e = espnow.ESPNow()
e.active(True)

# Adresse MAC de l'ESP32 robot
mac_robot = b'@L\xcaV\xbe,'  # ← à adapter selon ton robot
e.add_peer(mac_robot)

# Joystick
vrx = ADC(Pin(3))  # Axe X
vry = ADC(Pin(0))  # Axe Y
vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)
sw = Pin(1, Pin.IN, Pin.PULL_UP)

# Zone morte
DEAD_ZONE = 200
CENTER = 2400

# Fonction de direction
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

# Boucle principale
while True:
    x = vrx.read()
    y = vry.read()
    sw_val = sw.value()

    direction = get_direction(x, y)
    bouton = "pressé" if sw_val == 0 else "relâché"

    message = direction + "|" + bouton
    print("Envoi:", message)
    e.send(mac_robot, message)

    # Attente d'une réponse du robot (avec timeout)
    t0 = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), t0) < 300:
        host, msg = e.recv()
        if msg:
            led_msg = msg.decode()
            print("Reçu:", led_msg)
            if led_msg == "ROUGE":
                redled.value(1)
                greenled.value(0)
            elif led_msg == "VERT":
                redled.value(0)
                greenled.value(1)
            else:
                redled.value(0)
                greenled.value(0)
            break
    time.sleep(0.1)
