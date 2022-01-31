import requests
from sense_hat import SenseHat
sense = SenseHat()

readKey = "IABJ66QWGGLDHZ4O"
channelNumber = "1643637"
url = "https://api.thingspeak.com/channels/" + channelNumber + "/feeds.json"
results = 2

def main():
    # payload includes the headers to be sent with the GET request
    # read the documentation for more information (https://docs.python-requests.org)
    payload = {'api_key': readKey, 'results': results}

    # Sends an HTTP GET request
    response = requests.get(url, params=payload)
    response = response.json()

    print("Channel Name: {}".format(response['channel']['name']))
    
    entries = response['feeds']

    # Print out the temperature at each entry's time
    for e in entries:
        print("At {}, the temperature was {}".format(e['created_at'], e['field1']))
        print("At {}, the humidity was {}".format(e['created_at'], e['field2']))
        print("At {}, the pressure was {}".format(e['created_at'], e['field3']))
        
    message = "At {}, the temperature was {}".format(e['created_at'], e['field1']) + "At {}, the humidity was {}".format(e['created_at'], e['field2']) + "At {}, the pressure was {}".format(e['created_at'], e['field3'])
    sense.show_message(message,scroll_speed=0.05)    

if __name__ == "__main__":
    main()
