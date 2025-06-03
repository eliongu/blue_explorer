import network
import espnow
from machine import ADC, Pin
import time

# LEDs
greenled = Pin(5, Pin.OUT)
redled = Pin(4, Pin.OUT)

<<<<<<< HEAD
# Initialisation Wi-Fi
sta = network.WLAN(network.STA_IF)
=======
# ESP-NOW
sta = network.WLAN(network.WLAN.IF_STA)
>>>>>>> 390f6a88c2312db33467bf4a244609455c93b866
sta.active(True)
sta.disconnect()

# Initialisation ESP-NOW
e = espnow.ESPNow()
e.active(True)

<<<<<<< HEAD
macC6 = b'@L\xcaV\xbe,'
e.add_peer(macC6)


vrx = ADC(Pin(3))  
vry = ADC(Pin(0))  
vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)


sw = Pin(1, Pin.IN, Pin.PULL_UP)


=======
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
>>>>>>> 390f6a88c2312db33467bf4a244609455c93b866
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
<<<<<<< HEAD
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
=======
>>>>>>> 390f6a88c2312db33467bf4a244609455c93b866
    x = vrx.read()
    y = vry.read()
    sw_val = sw.value()

    direction = get_direction(x, y)
    bouton = "pressé" if sw_val == 0 else "relâché"

<<<<<<< HEAD
    # Envoi du message
    message = direction + "|" + bouton
    print("Envoi:", message)
    e.send(macC6, message)

    time.sleep(0.3)
=======
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
>>>>>>> 390f6a88c2312db33467bf4a244609455c93b866
