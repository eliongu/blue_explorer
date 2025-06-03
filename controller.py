import network
import espnow
from machine import ADC, Pin
import time

# LEDs
greenled = Pin(5, Pin.OUT)
redled = Pin(4, Pin.OUT)

# Initialisation Wi-Fi
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()

# Initialisation ESP-NOW
e = espnow.ESPNow()
e.active(True)

macC6 = b'@L\xcaV\xbe,'
e.add_peer(macC6)


vrx = ADC(Pin(3))  
vry = ADC(Pin(0))  
vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)


sw = Pin(1, Pin.IN, Pin.PULL_UP)


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
    print("Début de boucle")
    recv = e.recv()
    print("Réception vérifiée")
    if recv:
        host, msg = recv
        try:
            ledlight = msg.decode()
            if ledlight == "ROUGE":
                print("LED Rouge")
                redled.value(1)
                greenled.value(0)
            elif ledlight == "VERT":
                print("LED Verte")
                redled.value(0)
                greenled.value(1)
            else:
                print("Aucune LED")
        except Exception as ex:
            print("Erreur de décodage :", ex)
    else:
        print("Aucun message reçu")

    # Lecture joystick
    x = vrx.read()
    y = vry.read()
    sw_val = sw.value()

    direction = get_direction(x, y)
    bouton = "pressé" if sw_val == 0 else "relâché"

    # Envoi du message
    message = direction + "|" + bouton
    print("Envoi:", message)
    e.send(macC6, message)

    time.sleep(0.3)
