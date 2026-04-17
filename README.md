# Rideau Canal Sensor Simulation

## Overview

This project simulates IoT sensors deployed at multiple locations along the Rideau Canal Skateway in Ottawa.  
The simulator generates realistic environmental telemetry data and sends it to Azure IoT Hub at regular intervals for real-time processing.

The simulated data is used as the input source for a real-time monitoring and visualization system that evaluates ice safety conditions along the canal.

---

## Technologies Used

- Python 3
- Azure IoT Hub
- Azure IoT Device SDK for Python
- python-dotenv

---

## Prerequisites

Before running this sensor simulator, the following must be configured:

- An active Azure IoT Hub
- Three registered IoT devices representing canal locations:
  - `dows-lake`
  - `fifth-avenue`
  - `nac`
- Devices must use **symmetric key authentication**
- Python 3.x installed locally

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/rideau-canal-sensor-simulation.git
   cd rideau-canal-sensor-simulation



