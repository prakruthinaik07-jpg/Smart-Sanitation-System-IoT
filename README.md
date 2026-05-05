Smart Sanitation System (IoT)

An IoT-based Smart Sanitation System built using Raspberry Pi Pico W to monitor hygiene conditions in real-time.

---

Features

- Room Occupancy Detection using IR Sensors
- Entry and Exit Counting with Servo Door Control
- Dustbin Fill Level Monitoring using Ultrasonic Sensor
- Water Level Monitoring
- Gas and Odor Detection using MQ Sensor
- Cloud Integration using ThingSpeak
- Real-time data display on I2C LCD

---

Hardware Used

- Raspberry Pi Pico W
- IR Sensors
- Ultrasonic Sensors (HC-SR04)
- Gas Sensor (MQ Series)
- Servo Motor
- I2C LCD (16x2)
- Jumper Wires and Power Supply

---

Step-by-Step Working

1️⃣ Entry / Exit Detection
IR sensors are placed at the entrance.
When a person enters, the count increases.
When a person exits, the count decreases.
A servo motor controls the door automatically.
This helps track usage and control access.

2️⃣ Room Occupancy Monitoring
IR sensors inside each room detect presence.
If a person is inside, the room status is set to Occupied.
If no person is detected, the room status is set to Available.
Users can check availability before entering.

3️⃣ Dustbin Level Monitoring
An ultrasonic sensor measures the distance to waste.
If the distance is small, it indicates that the bin is full.
The system generates a cleaning alert.

4️⃣ Water Level Monitoring
An ultrasonic sensor measures the water tank level.
If the water level is low, an alert is generated.
This ensures water availability for users.

5️⃣ Gas / Odor Detection
A gas sensor (MQ series) detects harmful gases or bad smell.
If the threshold exceeds, a hygiene alert is triggered.
This improves sanitation awareness.

6️⃣ LCD Display (Local Monitoring)
The LCD displays real-time data such as:
Entry count
Room status
Bin level
Water level
Gas level
This helps users understand the condition before using the facility.

7️⃣ Cloud Integration (ThingSpeak)
All sensor data is sent to ThingSpeak.
The data is visualized as graphs in real time.
This enables remote monitoring and analysis.

8️⃣ Alert System
Alerts are generated when:
The bin is full
Water level is low
Gas level is high
Usage exceeds a defined limit
This helps the maintenance team take timely action.

---

Software and Tools

- MicroPython
- Thonny IDE
- ThingSpeak Cloud Platform

---

Output (ThingSpeak)

- Room occupancy data visualization
- Gas level monitoring
- Dustbin fill level tracking
- Water level monitoring
- Cleaning alert system

---

Project Demo

<img width="720" height="1600" alt="image" src="https://github.com/user-attachments/assets/14ff71df-6dda-4892-9e0c-476876dc3924" />
<img width="1600" height="897" alt="image" src="https://github.com/user-attachments/assets/0e54f399-60be-45e8-a362-1bfcb42f66a5" />
<img width="1599" height="1599" alt="image" src="https://github.com/user-attachments/assets/a69ed931-078b-4ddd-9384-295d833429ce" />
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/74fd4a7a-b9af-4643-8962-712e847e2419" />
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/7f90868e-4375-428c-8c22-a03912c9afc5" />


---

Author

Prakruthi. H N
