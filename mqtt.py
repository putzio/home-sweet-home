#  https://www.emqx.com/en/blog/how-to-use-mqtt-in-python

import random
import time
from dataclasses import dataclass
from queue import Queue
from paho.mqtt import client as mqtt_client
from threading import Thread

broker = "broker.emqx.io"
port = 1883
topic = "python/mqtt"
# Generate a Client ID with the subscribe prefix.
client_id = f"subscribe-{random.randint(0, 1000)}"
service_name = "python"
# username = 'emqx'
# password = 'public'


@dataclass
class Endpoint:
    topic: str
    on_message: callable


@dataclass
class MqttMessage:
    service_name: str
    topic: str
    data: str


class MQTT:
    def __init__(self, service_name: str, client_id=client_id):
        self.__connect_mqtt(client_id)
        self.__subscribing_thread = None
        self.__publishing_thread = None
        self.publishing_queue = Queue()
        self.service_name = service_name

    def get_topic(self, topic: str, service_name: str = None):
        if service_name is None:
            service_name = self.service_name
        return f"{service_name}/{topic}"

    def subscribe(self, topic: str, on_message: callable):
        if on_message is None:
            on_message = self.__print_on_message
        self.client.subscribe(self.get_topic(topic))
        self.client.on_message = on_message

    def publishing_message(self, message: MqttMessage):
        self.publishing_queue.put(message)

    def loop_forever(self):
        if self.__subscribing_thread is None:
            self.__subscribing_thread = Thread(target=self.client.loop_forever, daemon=True)
            self.__subscribing_thread.start()
        if self.__publishing_thread is None:
            self.__publishing_thread = Thread(target=self.__publishing_loop, daemon=True)
            self.__publishing_thread.start()

    def __publishing_loop(self):
        while True:
            time.sleep(1)
            if self.publishing_queue.empty():
                continue
            message = self.publishing_queue.get()
            topic = self.get_topic(message.topic, message.service_name)
            data = message.data
            result = self.client.publish(topic, data)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(f"Send `{data}` to topic `{topic}`")
            else:
                print(f"Failed to send message to topic {topic}")

    def __connect_mqtt(self, client_id=client_id):
        self.client = mqtt_client.Client(client_id)
        # client.username_pw_set(username, password)
        self.client.on_connect = self.__on_connect
        self.client.connect(broker, port)

    def __on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    def __print_on_message(self, client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")


if __name__ == "__main__":

    def run():
        mqtt = MQTT(client_id=client_id, service_name=service_name)
        mqtt.subscribe(topic, None)
        mqtt.loop_forever()
        while True:
            time.sleep(1)

    run()
