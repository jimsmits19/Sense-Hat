import subprocess
import time

def __cpu_temperature():
    raw_cpu_temp = subprocess.check_output("vcgencmd measure_temp", shell=True)
    cpu_temp = str(raw_cpu_temp).split('=')[1].split("'")[0]
    return float(cpu_temp)

while True:

    try:
        logfile = open("/home/pi/fan/log.txt", "a+")        
        temp = str(__cpu_temperature())
        logfile.write(temp + "\r\n")
        print(temp)
        time.sleep(60)
             
    except Exception as e:
        logfile.write(str(e) + "\r\n")
    finally:
        logfile.close()
