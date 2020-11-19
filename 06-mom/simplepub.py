# import library paho mqtt
import paho.mqtt.client as mqtt

# Inisiasi mqtt client
client = mqtt.Client(client_id="pub1", clean_session=False)

# Buat koneksi ke broker
client.connect("34.233.135.154", port=1883)

# Publish message
client.publish("/suhu/1", payload="Selamat Siang", qos=1)