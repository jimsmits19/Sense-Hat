import humi
import temp

from sense_hat import SenseHat
sense = SenseHat()

def main():
    humi.display_humidity()
    humi.send_humidity()
    temp.display_temperature()
    temp.send_temperature()

while True:
    event = sense.stick.wait_for_event()
    if event.action == 'pressed' :
        main()
