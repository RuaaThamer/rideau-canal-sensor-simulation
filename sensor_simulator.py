import os
import json
import time
import random
from datetime import datetime, timezone

from azure.iot.device import IoTHubDeviceClient, Message
from dotenv import load_dotenv

load_dotenv()

DEVICE_CONNECTIONS = {
    "dows-lake": os.getenv("IOTHUB_DEVICE_CONN_DOWS"),
    "fifth-avenue": os.getenv("IOTHUB_DEVICE_CONN_FIFTH"),
    "nac": os.getenv("IOTHUB_DEVICE_CONN_NAC")
}

SEND_INTERVAL = int(os.getenv("SEND_INTERVAL_SECONDS", 10))

for device, conn in DEVICE_CONNECTIONS.items():
    if not conn:
        raise ValueError(f"Missing connection string for {device}")

def create_clients():
    clients = {}
    for location, conn_str in DEVICE_CONNECTIONS.items():
        client = IoTHubDeviceClient.create_from_connection_string(conn_str)
        clients[location] = client
    return clients

def generate_sensor_data(location):
    return {
        "location": location,
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "iceThicknessCm": round(random.uniform(24.0, 40.0), 1),
        "surfaceTemperatureC": round(random.uniform(-10.0, 2.0), 1),
        "snowAccumulationCm": round(random.uniform(0.0, 5.0), 1),
        "externalTemperatureC": round(random.uniform(-15.0, 5.0), 1)
    }

def send_message(client, data, location):
    payload = json.dumps(data)
    message = Message(payload)
    message.content_type = "application/json"
    message.content_encoding = "utf-8"
    client.send_message(message)
    print(f"[{location}] Message sent at {data['timestamp']}")

def main():
    print("Starting Rideau Canal Sensor Simulator...")
    clients = create_clients()

    try:
        while True:
            for location, client in clients.items():
                data = generate_sensor_data(location)
                send_message(client, data, location)

            print(f"Sleeping for {SEND_INTERVAL} seconds...\n")
            time.sleep(SEND_INTERVAL)

    except KeyboardInterrupt:
        print("Simulation stopped by user.")

    finally:
        for client in clients.values():
            client.shutdown()

if __name__ == "__main__":
    main()
