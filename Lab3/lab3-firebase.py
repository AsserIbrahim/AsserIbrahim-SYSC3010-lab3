import pyrebase
import random
import time
from sense_hat import SenseHat
from time import sleep



# Create new Firebase config and database object
config = {
  "apiKey": "AIzaSyCitfQVdHfP9AE_fghH_7KRP5JNLoMMUOE",
  "authDomain": "lab3-15ef8.firebaseapp.com",
  "databaseURL": "https://lab3-15ef8-default-rtdb.firebaseio.com/",
  "storageBucket": "lab3-15ef8.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
dataset = "sensor1"

# Write random numbers to database
def writeData():
  key = 0
  while True:
    # I'm using dummy sensor data here, you could use your senseHAT
        sensorData = SenseHat()
        temperature = sensorData.get_temperature()
        pressure = sensorData.get_pressure()
        humidity = sensorData.get_humidity()
        
        dictionnary = {'Temperature': temperature, 'Humidity': humidity, 'Pressure': pressure}
        db.child(dataset).child(key).set(dictionnary)
        key = key + 1
        time.sleep(1)

def readData():
  # Returns the entry as an ordered dictionary (parsed from json)
    config = {
      "apiKey": "AIzaSyCitfQVdHfP9AE_fghH_7KRP5JNLoMMUOE",
      "authDomain": "lab3-15ef8.firebaseapp.com",
      "databaseURL": "https://lab3-15ef8-default-rtdb.firebaseio.com/",
      "storageBucket": "lab3-15ef8.appspot.com"
     }
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    dataset = "sensor1"
    mySensorData = db.child(dataset).get()
    print(mySensorData.val())
    print("Parent Key: {}".format(mySensorData.key()))
    print("Parent Value: {}\n".format(mySensorData.val()))
    # Returns the dictionary as a list
    mySensorData_list = mySensorData.each()
    # Takes the last element of the list
    lastDataPoint = mySensorData_list[-1]
    print("Child Key: {}".format(lastDataPoint.key()))
    print("Child Value: {}\n".format(lastDataPoint.val()))

def main():
    
     #writeData()
     readData()
    
if __name__== "__main__":
    main()
    