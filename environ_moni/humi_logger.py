import humi
from datetime import datetime

humi.send_humidity()
print("humidity sent at " + str(datetime.now()))
