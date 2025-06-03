from motors import *
from ultrasound import *
from autonomous import *
from monitor import *

while True:
    monitor()
    while autonomous_mode:
        monitor()
        explore()
