import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

while True:
    i=GPIO.input(11)
    if i==0:
        time.sleep(0.1)
    elif i==1:
        print("motion detected @",datetime.now().strftime("%H:%M:%S"))
        time.sleep(30)