import requests
from time import sleep
import paho.mqtt.client as mqtt
from sys import exit
from os import environ


def main():

    data_url = environ.get('DATA_URL', "http://10.42.20.255/csv.html")
    broker = environ.get('BROKER', "mqtt.shack")
    clientname = "shackstrom"
    topic = "glados/" + clientname + "/"

    client = mqtt.Client(clientname)
    client.connect(broker)
    client.publish(topic + "status", payload="Online", qos=0, retain=True)
    client.will_set(topic + "status", payload="Offline", qos=0, retain=True)
    print(f"connected to {broker}")
    while True:
        try:
            r = (requests.get(data_url).text)
            data = r.split("body")[1].split(",")
            zaehlerstand_foyer = int(data[16]) * 10  # in Wh
            zaehlerstand_kueche = int(data[17]) * 10  # in Wh
            zaehlerstand_c2 = int(data[18]) * 10  # in Wh

            client.publish(topic + "zaehler_foyer/total", zaehlerstand_foyer)
            client.publish(topic + "zaehler_kueche/total", zaehlerstand_kueche)
            client.publish(topic + "zaehler_c2/total", zaehlerstand_c2)
            client.publish(topic + "total",
                           zaehlerstand_foyer
                           + zaehlerstand_kueche
                           + zaehlerstand_c2)

            sleep(60)  # wait a minute
        except KeyboardInterrupt:
            break
    print("computer kaputt, bitte neustarten")
    exit(1)


if __name__ == "__main__":
    main()
