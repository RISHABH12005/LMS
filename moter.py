from brickpi3 import BrickPi3
import time

BP = BrickPi3()
motor_C = BP.PORT_A  # Motor C -> port C
motor_B = BP.PORT_D  # Motor B -> port B

def move(direction):
    try:
        command = direction.lower()
        
        if command == 'cw':
            print("Setting motor_C (C) to 50 and motor_B (B) to -50")
            BP.set_motor_power(motor_C, 50)
            BP.set_motor_power(motor_B, -50)
            time.sleep(0.5)
            print("Stopping motors.")
            BP.set_motor_power(motor_C, 0)
            BP.set_motor_power(motor_B, 0)
        
        elif command == 'ccw':
            print("Setting motor_C (C) to -50 and motor_B (B) to 50")
            BP.set_motor_power(motor_C, -50)
            BP.set_motor_power(motor_B, 50)
            time.sleep(0.5)
            print("Stopping motors.")
            BP.set_motor_power(motor_C, 0)
            BP.set_motor_power(motor_B, 0)
        
        elif command == 'e':
            print("Exiting...")
            BP.set_motor_power(motor_C, 0)
            BP.set_motor_power(motor_B, 0)
            return
        
        else:
            print("Invalid command! Please use 'cw' (clockwise), 'ccw' (counterclockwise), or 'e' (exit).")
    
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    
    finally:
        BP.set_motor_power(motor_C, 0)
        BP.set_motor_power(motor_B, 0)
        BP.reset_all()

'''
#Example usage
while True:
    direction = input("Enter command (cw/ccw/e): ")
    if direction.lower() == 'e':
        break
    move(direction)
'''