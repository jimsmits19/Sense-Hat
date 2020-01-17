import web_methods
from sense_hat import SenseHat

_sense = SenseHat()
_sense.clear()
    
def print_humidity():
    print("humi:" + str(__humidity()))

def display_humidity():
    _sense.show_message(str(__humidity()))    

def send_humidity():
    data = { 'humidity': __humidity() }
    web_methods.post("https://jasoncases.zerodock.com/module/envmonitor/humidity", data) 

def retrieve_humidity():
    humidity = web_methods.get("https://jasoncases.zerodock.com/module/envmonitor/humidity")
    return str(humidity)

def __humidity():
    humidity = _sense.get_humidity()
    return round(humidity, 1)
