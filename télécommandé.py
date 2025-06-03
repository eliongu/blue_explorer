import network
import espnow
from machine import Pin, PWM
from time import sleep

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

# --- Fonctions moteurs ---
def set_speed(percent, enable):
    duty = int((percent / 100) * 1023)
    enable.duty(duty)

def motorD_forward():
    pin1.value(0)
    pin2.value(1)

def motorD_backward():
    pin1.value(1)
    pin2.value(0)

def motorG_forward():
    pin3.value(0)
    pin4.value(1)

def motorG_backward():
    pin3.value(1)
    pin4.value(0)

def forward():
    print("Avancer")
    set_speed(80, enable1)
    set_speed(80, enable2)
    motorD_forward()
    motorG_forward()

def backward():
    print("Reculer")
    set_speed(80, enable1)
    set_speed(80, enable2)
    motorD_backward()
    motorG_backward()

def turn_left():
    print("Gauche")
    set_speed(80, enable1)
    set_speed(80, enable2)
    motorG_backward()
    motorD_forward()

def turn_right():
    print("Droite")
    set_speed(80, enable1)
    set_speed(80, enable2)
    motorG_forward()
    motorD_backward()

def stop():
    print("Stop")
    pin1.value(0)
    pin2.value(0)
    pin3.value(0)
    pin4.value(0)
    set_speed(0, enable1)
    set_speed(0, enable2)

# --- Boucle principale : écoute des messages ---
while True:
    host, msg = e.recv()
    if msg:
        try:
            direction, bouton = msg.decode().split("|")
            print("Reçu:", direction, "|", bouton)

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
            

