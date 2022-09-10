import RPi.GPIO as GPIO
import time
import csv
from datetime import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

column_name = ["DateTime", "Sensor"] 

with open('./logs/detect.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(column_name) 

while True:
    i=GPIO.input(11)
    if i==0:
        time.sleep(0.1)
    elif i==1:
        print("motion detected @",datetime.now().strftime("%H:%M:%S"))
        with open('./logs/detect.csv', 'a') as f:
            writer = csv.writer(f)
            #writer.writerow(column_name) 
            data = [datetime.now().strftime("%H:%M:%S"),"Sensor1"]
            writer.writerow(data)
        time.sleep(0.1)