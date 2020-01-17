import web_methods
import subprocess
from sense_hat import SenseHat

_sense = SenseHat()
_sense.clear()




def print_temperature():
    print("temp:" + str(__temperature()))

def display_temperature():
    _sense.show_message(str(__temperature()))

def send_temperature():
    data = {
        'temperature': __temperature(),
        'cpu_temperature': __cpu_temperature()
    }
    web_methods.post("https://jasoncases.zerodock.com/module/envmonitor/temperature", data)



def retrieve_temperature():
    return str(web_methods.get("https://jasoncases.zerodock.com/module/envmonitor/temperature"))

def __temperature():
    temperature = _sense.get_temperature()
    return __to_fahrenheit(temperature)

def __cpu_temperature():
    raw_cpu_temp = subprocess.check_output("vcgencmd measure_temp", shell=True)
    cpu_temp = str(raw_cpu_temp).split('=')[1].split("'")[0]
    return __to_fahrenheit(float(cpu_temp))

def __to_fahrenheit(centigrade):
    return round((centigrade * 9/5 +32), 1)
