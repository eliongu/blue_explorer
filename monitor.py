import network
import espnow
from motors import *

sta = network.WLAN(network.WLAN.IF_STA)
sta.active(True)
sta.disconnect()

e = espnow.ESPNow()
e.active(True)

pin1 = Pin(10, Pin.OUT)
pin2 = Pin(8, Pin.OUT)
enable1 = PWM(Pin(7))
enable1.freq(1000)

pin3 = Pin(22, Pin.OUT)
pin4 = Pin(23, Pin.OUT)
enable2 = PWM(Pin(21))
enable2.freq(1000)

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
                
            if not autonomous_mode:
            # Action selon direction
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