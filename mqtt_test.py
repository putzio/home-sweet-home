from mqtt import MQTT, MqttMessage
from time import sleep

topic = "python/mqtt"
client_id = f"subscribe-{100}"
remote_service = "python"

mqtt = MQTT(service_name="python1", client_id=client_id)
mqtt.subscribe(topic, None)
mqtt.loop_forever()
while True:
    sleep(1)
    mqtt.publishing_message(MqttMessage(remote_service, topic, "Hello world!"))
