# Livestock Monitoring System

## Overview

The *Livestock Monitoring System* is an advanced solution designed to improve livestock management & ensure their well-being. By utilizing modern technology, this system helps farmers efficiently track livestock movements, monitor their health, detect obstacles in their surroundings using a combination of sensors & automation tools.

This system integrates *Raspberry Pi 3B, BrickPi, LEGO Mindstorms motors, ultrasonic sensors, web camera* to enable real-time monitoring & automated operations. It enhances efficiency by detecting obstacles, automating movement, providing remote access to livestock data.

## Hardware Components

| Component                   | Function                                                |
| --------------------------- | ------------------------------------------------------- |
| *Raspberry Pi 3B (1GB RAM)* | Controls the entire system                              |
| *BrickPi*                   | Interfaces Raspberry Pi with LEGO Mindstorms components |
| *Web Camera*                | Captures live video feed                                |
| *2 Ultrasonic Sensors*      | Detects obstacles at the front & back                |
| *2 LEGO Mindstorms Motors*  | Controls movement of gates & feeding systems         |

## Features

For our prototype, we are using a *website* to control the motors remotely & display real-time video feed directly on the web interface.

- *Live Camera Feed* – Enables remote livestock monitoring through a web camera.
- *Obstacle Detection* – Uses ultrasonic sensors to detect & respond to obstacles.
- *Motorized Control* – Automates movement using LEGO Mindstorms motors.
- *Alert System* – Sends real-time notifications when obstacles are detected.

## Software & Libraries

- *Python* – Manages motor control & obstacle detection
- *Uvicorn* – ASGI server for running FastAPI applications
- *Websockets* – Facilitates real-time communication
- *Ngrok* – Enables secure remote access
- *BrickPi* – Interfaces Raspberry Pi with LEGO Mindstorms components
- *FastAPI* – Provides a high-performance API framework
- *OpenCV* – Handles image processing & computer vision tasks
- *Torch* – Supports AI/ML functionalities
- *Ultralytic* – Offers advanced data analytics

## Expected Output

- Real-time tracking of livestock movements
- Automated obstacle detection & response
- Control of gates & feeding systems
- Remote access to live video feed & system alerts

## Future Enhancements

- *Sense HAT* for collecting environmental data
- *Raspberry Pi AI Hat* for enhanced AI-based analytics
- *Thermal Camera* for livestock health monitoring based on temperature
- *Motion Sensor* for improved movement detection
- AI-driven livestock health analysis
- Remote control capabilities via a mobile app
- Cloud-based data storage & analytics for better decision-making
