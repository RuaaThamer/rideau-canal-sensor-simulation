# Rideau Canal IoT Sensor Simulation

## 1. Overview

This repository contains the IoT sensor simulation component of the Rideau Canal Real‑Time Monitoring System.  
The simulator emulates multiple environmental sensors deployed along different locations of the Rideau Canal and continuously sends telemetry data to Azure IoT Hub.

The simulated data represents key environmental conditions related to ice safety, and serves as the ingestion source for real‑time analytics, storage, and dashboard visualization.

---

## Technologies Used

- **Python 3.x**
- **Azure IoT Hub SDK for Python**
- **JSON** for telemetry message formatting
- **dotenv** for environment variable management

---

## 2. Prerequisites

Before running the simulator, ensure you have:

- Python 3.x installed
- An active Azure subscription
- An Azure IoT Hub instance
- IoT devices registered in Azure IoT Hub
- Device connection strings available

---

## 3. Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RuaaThamer/rideau-canal-sensor-simulation.git
   cd rideau-canal-sensor-simulation

## Install required Python dependencies:
pip install -r requirements.txt

## 4. Configuration
1. Create a .env file using the provided example: cp .env.example .env
2. Update .env with your Azure IoT Hub device connection strings:
DOWS_LAKE_CONNECTION_STRING=your-connection-string
FIFTH_AVENUE_CONNECTION_STRING=your-connection-string
NAC_CONNECTION_STRING=your-connection-string    
3. Sensor locations and simulation parameters can be modified in: config/sensor_config.json

## 5. Usage 
To start the sensor simulation, run:
python sensor_simulator.py
The simulator will:

Generate telemetry data for each configured location
Send messages every 10 seconds
Continuously stream data to Azure IoT Hub

Console output will confirm successful message transmission.

## 6. Code Structure

<img width="242" height="197" alt="image" src="https://github.com/user-attachments/assets/cb0ec659-07ee-445c-99ee-600c4c80de87" />


Main Components


sensor_simulator.py

**Main entry point**
Generates and sends telemetry messages
Manages multiple simulated sensors

sensor_config.json

Defines sensor locations and simulation parameters

**Key Functions**

Telemetry generation function
Randomized environmental value simulation
Azure IoT Hub message transmission
Timed loop for periodic data sending

## 7.Sensor Data Format
JSON Schema 

{
  "location": "dows-lake",
  "timestamp": "2026-04-18T14:35:00Z",
  "iceThicknessCm": 32.5,
  "surfaceTemperatureC": -3.2,
  "snowAccumulationCm": 4.0,
  "externalTemperatureC": -7.8
}

Example Output
{
  "location": "nac",
  "timestamp": "2026-04-18T14:45:10Z",
  "iceThicknessCm": 28.7,
  "surfaceTemperatureC": -1.5,
  "snowAccumulationCm": 6.3,
  "externalTemperatureC": -5.9
}

## 8. Troubleshooting


| Issue                     | Solution                                              |
|--------------------------|-------------------------------------------------------|
| Connection error         | Verify IoT Hub connection strings                     |
| No messages in IoT Hub   | Confirm device registration and credentials           |
| Python module not found  | Re‑install dependencies using `pip install -r requirements.txt` |
| Simulator stops unexpectedly | Check `.env` file and JSON configuration validity |
