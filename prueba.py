import requests

URL = "http://127.0.0.1/test_axotec/prueba.php"

serie_data = 111
accelx_data = 5.22
accely_data = '1.21'
accelz_data = '1.21'


form_data = {'serie': serie_data,
            'accelx': accelx_data,
            'accely': accely_data,
            'accelz': accelz_data}

server = requests.post(URL, data=form_data)

output = server.text

print('The response from the server is: \n', output)