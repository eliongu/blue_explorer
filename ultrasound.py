from machine import Pin, time_pulse_us
import time

SOUND_SPEED= 340
TRIG_PULSE_DURATION_US=10

trig_pin1 = Pin(18, Pin.OUT)
echo_pin1 = Pin(11, Pin.IN)

trig_pin2 = Pin(5, Pin.OUT)
echo_pin2 = Pin(4, Pin.IN)


global distance_front
global distance_back

def get_distance():
    trig_pin1.value(0)
    trig_pin2.value(0)
    time.sleep_us(5)
    # Créer une impulsion de 10 µs
    trig_pin1.value(1)
    trig_pin2.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig_pin1.value(0)
    trig_pin2.value(0)

    ultrason_duration1 = time_pulse_us(echo_pin1, 1, 30000) # Renvoie le temps de propagation de l'onde (en µs)
    ultrason_duration2 = time_pulse_us(echo_pin2, 1, 30000)

    distance_front = SOUND_SPEED * ultrason_duration1 / 20000
    distance_back = SOUND_SPEED * ultrason_duration2 / 20000


    # print(f"Distance  front : {distance_front} cm")
    print(f"Distance back : {distance_back} cm")
    time.sleep_ms(500)
    return distance_front, distance_back