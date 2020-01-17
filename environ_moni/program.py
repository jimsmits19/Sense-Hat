import temp
import humi
import time
from datetime import datetime

print("environmental monitoring started at " + str(datetime.now()))

def log_humidity():
    humi.send_humidity()

def log_temperature():
    temp.send_temperature()

while True:

    try:
        logfile = open("/home/pi/environ_moni/program_log.txt", "a+")
        log_humidity()
        logfile.write("humi logged at " + str(datetime.now()) + "\r\n")
        log_temperature()
        logfile.write("temp logged at " + str(datetime.now()) + "\r\n")
        time.sleep(60)
             
    except Exception as e:
        logfile.write(str(e) + "\r\n")
        time.sleep(30)
    finally:
        logfile.close()


