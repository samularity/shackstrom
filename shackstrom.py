import requests
from time import sleep
import paho.mqtt.client as mqtt
from sys import exit


def main():
    client = mqtt.Client("shackstrom")
    client.connect("mqtt.shack")
    client.publish("glados/shackstrom/status", payload="Online", qos=0, retain=True)
    client.will_set("glados/shackstrom/status", payload="Offline", qos=0, retain=True)
    print("conneted to mqtt.shack")
    while True:
        try:
            r = (requests.get("http://10.42.20.255/csv.html").text)
            data = r.split("body")[1].split(",")
            zaehlerstand_foyer = int(data[16]) * 10  # in Wh
            zaehlerstand_c2 = int(data[18]) * 10  # in Wh

            client.publish("glados/shackstrom/zaehler_foyer/total", zaehlerstand_foyer)
            client.publish("glados/shackstrom/zaehler_c2/total", zaehlerstand_c2)

            sleep(60)  # wait a minute
        except KeyboardInterrupt:
            break
    print("compute kaputt, bitte neustarten")
    exit(1)


if __name__ == "__main__":
    main()
