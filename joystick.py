from machine import ADC, Pin
import time

# Initialisation des axes
vrx = ADC(Pin(3))  # X
vry = ADC(Pin(0))  # Y
vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)

# Bouton
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

    print("X:{:<4} Y:{:<4} → {:<7} | Bouton: {}".format(x, y, direction, bouton)) #formatage pour meilleure lisibilité dans la console

    time.sleep(0.2)
