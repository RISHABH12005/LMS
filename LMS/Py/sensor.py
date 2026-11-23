import time
import brickpi3

BP = brickpi3.BrickPi3()
BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

time.sleep(1)
def sensor():
    try:
        try:
            distance_2 = BP.get_sensor(BP.PORT_2)  # Read sensor on PORT_2
            print(f"Sensor on PORT_2: {distance_2} cm")
        except brickpi3.SensorError as error:
            print(f"Sensor PORT_2 error: {error}")
        try:
            distance_4 = BP.get_sensor(BP.PORT_4)  # Read sensor on PORT_4
            print(f"Sensor on PORT_4: {distance_4} cm")
        except brickpi3.SensorError as error:
            print(f"Sensor PORT_4 error: {error}")
        time.sleep(1)
        
    except KeyboardInterrupt:
        BP.reset_all()
        print("Stopping program.")
