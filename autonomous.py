from ultrasound import *
from motors import *
import network
import espnow

sta = network.WLAN(network.WLAN.IF_STA) 
sta.active(True)
sta.disconnect() 

e = espnow.ESPNow()
e.active(True)
macC3 = b'hg%\xe8w\xe4'
e.add_peer(macC3)  




rotation_attempts = 0
MAX_ATTEMPTS = 3

def reset_attempts():
    global rotation_attempts
    rotation_attempts = 0

def check_obstacle():
    if distance_front < 10 and distance_back > 20:
        stop()
        backward()
        time.sleep(2)
        turn_left()
        time.sleep(1)
        stop()
        if distance_front < 10 and distance_back < 20:
            turn_left()
            time.sleep(2)
            stop()
            rotation_attempts += 1
        return False
    
    elif distance_front < 10 and distance_back < 10:
        stop()
        turn_right()
        time.sleep(1)
        stop()
        rotation_attempts += 1
        return False

    reset_attempts()
    return True
    
        

def explore():
    if rotation_attempts >= MAX_ATTEMPTS:
        print("Trop de tentatives. Le robot est peut-être bloqué.")
        stop()
        e.send(macC3, "ROUGE")
        return

    if check_obstacle():
        e.send(macC3, "VERT")
        forward()
    else:
        time.sleep(0.5)