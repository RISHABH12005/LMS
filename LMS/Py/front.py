from fastapi import FastAPI, WebSocket, Request
from fastapi.middleware.cors import CORSMiddleware
from picamera2 import Picamera2
import time
import cv2
import asyncio
import struct
from sense_hat import SenseHat
from datetime import datetime
from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput

picam2 = Picamera2()
picam2.preview_configuration.main.size = (144, 144)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()
app = FastAPI()
sense = SenseHat()
TEMP_CORRECTION = -2.0 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/sensor")
async def get_sensor_data():
    raw_temp = sense.get_temperature()
    temperature = raw_temp + TEMP_CORRECTION
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    return {
        "timestamp": datetime.now().isoformat(),
        "temperature": round(temperature, 2),
        "humidity": round(humidity, 2),
        "pressure": round(pressure, 2)
    }
@app.get("/")
async def root():
    return {"message": "WebSocket video server is running"}

@app.websocket("/share")
async def video_stream(websocket: WebSocket):
    await websocket.accept()
    print("Client Connected")

    try:
        await asyncio.sleep(2)

        while True:
            frame = picam2.capture_array()
            frame = cv2.rotate(frame, cv2.ROTATE_180)

            _, buffer = cv2.imencode(".jpg", frame)
            frame_bytes = buffer.tobytes()
            header = struct.pack("<Q", len(frame_bytes))

            await websocket.send_bytes(header + frame_bytes)
            print(f"Sent Frame ({len(frame_bytes)} bytes)")

            await asyncio.sleep(1 / 30)

    except Exception as e:
        print("WebSocket Error:", e)

    finally:
        try:
            if websocket.application_state.name != "DISCONNECTED":
                await websocket.close()
                print("WebSocket closed cleanly")
        except RuntimeError as ws_err:
            print("WebSocket already closed:", ws_err)

        print("Cleanup completed. Ready for next connection")