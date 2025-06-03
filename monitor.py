import network
import espnow
from motors import *

sta = network.WLAN(network.WLAN.IF_STA)
sta.active(True)
sta.disconnect()

e = espnow.ESPNow()
e.active(True)

autonomous_mode = False

def monitor():
    global autonomous_mode
    host, msg = e.recv()
    if msg:
        try:
            direction, bouton = msg.decode().split("|")
            print("Reçu:", direction, "|", bouton)

            if bouton == "pressé":
                autonomous_mode = not autonomous_mode
                sleep(0.2)  # Anti-rebond

            # Répondre à l'émetteur pour allumer la LED correspondante
            if autonomous_mode:
                e.send(host, b"VERT")
            else:
                e.send(host, b"ROUGE")

            if not autonomous_mode:
                if direction == "CENTRE":
                    stop()
                elif direction == "HAUT":
                    forward()
                elif direction == "BAS":
                    backward()
                elif direction == "GAUCHE":
                    turn_left()
                elif direction == "DROITE":
                    turn_right()
                else:
                    stop()

        except Exception as err:
            print("Erreur décodage :", err)
