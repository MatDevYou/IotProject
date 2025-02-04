from flask import Flask, render_template, request, jsonify
import paho.mqtt.client as mqtt
import os

app = Flask(__name__)

# Configurazione MQTT
MQTT_BROKER = os.getenv("MQTT_BROKER", "mqtt-broker")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = "test/topic"

# Configura client MQTT
client = mqtt.Client()

# Callback quando si riceve un messaggio
def on_message(client, userdata, msg):
    print(f"Ricevuto: {msg.payload.decode()} su {msg.topic}")

client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC)
client.loop_start()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/publish", methods=["POST"])
def publish():
    data = request.json
    topic = data.get("topic", MQTT_TOPIC)
    message = data.get("message", "Messaggio di test")
    client.publish(topic, message)
    return jsonify({"status": "success", "topic": topic, "message": message})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)