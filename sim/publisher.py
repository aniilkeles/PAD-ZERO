import json
import time
from datetime import datetime, timezone

import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "padzero/telemetry/pt_fuel"

# 1) Broker'a bağlan
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT)
client.loop_start()

pressure = 0.0
seq = 0

# 2) Sonsuza kadar: basıncı biraz artır, mesajı gönder, yarım saniye bekle
while True:
    pressure = min(pressure + 0.5, 25.0)
    seq += 1

    message = {
        "sensor" : "pt_fuel",
        "value" : round(pressure, 1),
        "unit" : "bar",
        "time" : datetime.now(timezone.utc).isoformat(),
        "seq" : seq
    }

    client.publish(TOPIC, json.dumps(message))
    print("gönderildi:", message)

    time.sleep(0.5)