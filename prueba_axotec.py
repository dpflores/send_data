from axotec.accelerometer import Accelerometer
import time
import requests

# Accelerometer configuration
accel = Accelerometer()
# First, accelerometer has to be calibrated
#accel.getOffset()

URL = "http://127.0.0.1/test_axotec/prueba.php" #localhost

URL = "http://192.168.88.190/test_axotec/prueba.php" #ACME0

URL = "http://10.0.0.99/test_axotec/prueba.php" #VPN Del laptop

URL = "http://192.168.88.187/test_axotec/prueba.php" #VPN Del laptop


nData = 1000
cuenta = 0

serie_data = '111'

while True:

    accelx_data = accel.getAx()
    accely_data = accel.getAy()
    accelz_data = accel.getAz()

    form_data = {'serie': serie_data,
            'accelx': accelx_data,
            'accely': accely_data,
            'accelz': accelz_data}

    server = requests.post(URL, data=form_data)

    cuenta += 1
    
    print(cuenta, accelx_data, accelx_data)

    time.sleep(0.5)

    #sending each 0.1 seconds