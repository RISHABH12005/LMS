from time import sleep
from brickpi3 import BrickPi3
BP = BrickPi3()

try:
    BP.set_motor_power(BP.PORT_B, 50)
    sleep(2)
    BP.set_motor_power(BP.PORT_B, 0)
    sleep(1)
    BP.set_motor_power(BP.PORT_A, -50)
    sleep(2)
    BP.set_motor_power(BP.PORT_A, 0)
    print("working")

except KeyboardInterrupt:
    BP.set_motor_power(BP.PORT_B, 0)

except IOError as error:
    print(error)
    
finally:
    BP.reset_all()
