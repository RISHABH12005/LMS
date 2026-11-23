import time
import brickpi3

BP = brickpi3.BrickPi3()
A = BP.PORT_A
B = BP.PORT_C
C = BP.PORT_B
D = BP.PORT_D

BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

time.sleep(1)

SAFE_DISTANCE = 25
DEFAULT_SPEED = 500

def is_front_clear():
    try:
        dist = BP.get_sensor(BP.PORT_2)
        print(f"Front distance: {dist} cm")
        return dist > SAFE_DISTANCE
    except brickpi3.SensorError:
        print("Error reading front ultrasonic sensor.")
        return False

def is_back_clear():
    try:
        dist = BP.get_sensor(BP.PORT_3)
        print(f"Back distance: {dist} cm")
        return dist > SAFE_DISTANCE
    except brickpi3.SensorError:
        print("Error reading back ultrasonic sensor.")
        return False

def forward(speed=DEFAULT_SPEED):
    
    print("Moving forward")
    BP.set_motor_dps(A, speed)
    BP.set_motor_dps(B, speed)
    BP.set_motor_dps(C, speed)
    BP.set_motor_dps(D, speed)
    #time.sleep(2.5)
    #print("turn off")
    #stop_motors()

def backward(speed=DEFAULT_SPEED):
    print("Moving backward")
    BP.set_motor_dps(A, -speed)
    BP.set_motor_dps(B, -speed)
    BP.set_motor_dps(C, -speed)
    BP.set_motor_dps(D, -speed)
    #time.sleep(2.5)
    #stop_motors()


def rotate_clockwise(speed=DEFAULT_SPEED):
    if is_front_clear():
        print("Rotating clockwise")
        BP.set_motor_dps(A, -speed)
        BP.set_motor_dps(B, -speed)
        BP.set_motor_dps(C, speed)
        BP.set_motor_dps(D, speed)
        #time.sleep(2.5)
        #stop_motors()
    else:
        print("Obstacle detected behind! Stopping.")
        stop_motors()
         
def rotate_anticlockwise(speed=DEFAULT_SPEED):
    if is_back_clear():
        print("Rotating anticlockwise")
        BP.set_motor_dps(A, speed)
        BP.set_motor_dps(B, speed)
        BP.set_motor_dps(C, -speed)
        BP.set_motor_dps(D, -speed)
        #time.sleep(2.5)
        #stop_motors()
    else:
        print("Obstacle detected behind! Stopping.")
        stop_motors()
        
def stop_motors():
    print("Stopping motors")
    BP.set_motor_power(A, 0)
    BP.set_motor_power(B, 0)
    BP.set_motor_power(C, 0)
    BP.set_motor_power(D, 0)

def move(direction):
    if direction == "a":
        forward()
    elif direction == "c":
        backward()
    elif direction == "b":
        rotate_clockwise()
    elif direction == "f":
        rotate_anticlockwise()
    elif direction == "s":
        stop_motors()
    elif direction == "e":
        stop_motors()
    else:
        print("Invalid command. Try again.")

try:
    while True:
        direction = input("Enter command (a-forward, c-backward, b-cw, f-ccw, s-stop, e-exit): ").strip().lower()
        if direction == "e":
            break
        move(direction)

except KeyboardInterrupt:
    print("Program interrupted by user.")

finally:
    stop_motors()
    BP.reset_all()
