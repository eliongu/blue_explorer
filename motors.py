from machine import Pin, PWM
from time import sleep

pin1 = Pin(10, Pin.OUT)
pin2 = Pin(8, Pin.OUT)
enable1 = PWM(Pin(7))
enable1.freq(1000)

pin3 = Pin(22, Pin.OUT)
pin4 = Pin(23, Pin.OUT)
enable2 = PWM(Pin(21))
enable2.freq(1000)


def set_speed(percent, enable):
    duty = int((percent / 100) * 1023)
    enable.duty(duty)

def motor1_forward():
    pin1.value(1)
    pin2.value(0)

def motor1_backward():
    pin1.value(0)
    pin2.value(1)

def motor2_forward():
    pin3.value(0)
    pin4.value(1)

def motor2_backward():
    pin3.value(1)
    pin4.value(0)

def forward():
    set_speed(80, enable1)
    set_speed(80, enable2)
    motor1_forward()
    motor2_forward()

def backward():
    set_speed(80, enable1)
    set_speed(80, enable2)
    motor1_backward()
    motor2_backward()

def turn_left():
    set_speed(80, enable1)
    set_speed(80, enable2)
    motor1_backward()
    motor2_forward()

def turn_right():
    set_speed(80, enable1)
    set_speed(80, enable2)
    motor1_forward()
    motor2_backward()

def stop():
    pin1.value(0)
    pin2.value(0)
    pin3.value(0)
    pin4.value(0)
    set_speed(0, enable1)
    set_speed(0, enable2)

print("Stop")
stop()

