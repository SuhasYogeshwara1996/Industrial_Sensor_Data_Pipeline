# 🏭 Industrial Sensor Data Pipeline

This project simulates real-time industrial sensor data (Temperature & Pressure) using OPC UA, stores it in a TimescaleDB time-series database, and visualizes it live in Grafana dashboards. It demonstrates a full end-to-end data pipeline commonly used in IIoT and process automation.

---

## 🚀 Features

- 🛰️ Real-time data simulation using OPC UA (via `asyncua`)
- 🗃️ Time-series storage using TimescaleDB (PostgreSQL extension)
- 📈 Live dashboarding and querying using Grafana
- ⚙️ Docker-based database and visualization setup
- 💻 Python client/server communication for OPC

---

## 🛠️ Tech Stack

| Layer       | Tool/Technology           |
|-------------|---------------------------|
| Simulation  | Python + `asyncua`        |
| Database    | TimescaleDB (Dockerized)  |
| Visualization | Grafana (Dockerized)   |
| Backend     | Python (`psycopg2`, `asyncio`) |
| Dev Tools   | Docker, VS Code, Git      |


