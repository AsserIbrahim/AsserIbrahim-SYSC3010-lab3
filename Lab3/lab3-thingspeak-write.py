from sense_hat import SenseHat
import requests
from time import sleep


sense = SenseHat()

sendKey = "UIBAJKO5KNRGXLFL"
url = "https://api.thingspeak.com/update"

def main():
    while True:
    
        temperature = sense.get_temperature()
        pressure = sense.get_pressure()
        humidity = sense.get_humidity()

    # payload includes the headers to be sent with the GET request
    # read the documentation for more information (https://docs.python-requests.org)
        payload = {'field1': temperature, 'field2': humidity, 'field3': pressure,'api_key': sendKey}
        try:
        # Sends an HTTP GET request
            response = requests.get(url, params=payload)
        # The library can also decode JSON responses
            response = response.json()

            print(response)
        except:
            print("Connection Failed")
        
        sleep(120)

if __name__ == "__main__":
    main()
